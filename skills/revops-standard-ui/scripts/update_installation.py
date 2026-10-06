#!/usr/bin/env python3
"""Install this skill from origin/main, with a seven-day check interval."""

import argparse
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import time

SKILL = "revops-standard-ui"
SOURCE = f"skills/{SKILL}"
INTERVAL = 7 * 24 * 60 * 60


def git(repo, *args):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], env=env, stderr=subprocess.PIPE,
        timeout=120,
    )


def fingerprint(folder):
    digest = hashlib.sha256()
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink in skill: {path}")
        if path.is_file():
            digest.update(path.relative_to(folder).as_posix().encode() + b"\0")
            digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def save(path, state):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, indent=2) + "\n")
    temporary.replace(path)


def validate(folder):
    text = (folder / "SKILL.md").read_text()
    if not text.startswith("---\n"):
        raise ValueError("Missing skill frontmatter")
    frontmatter = text.split("---", 2)[1]
    lines = frontmatter.splitlines()
    if f"name: {SKILL}" not in lines:
        raise ValueError("Unexpected skill name")
    if not any(line.startswith("description:") and line[12:].strip() for line in lines):
        raise ValueError("Missing skill description")
    if not (folder / "references/serval-design.md").is_file():
        raise ValueError("Missing Serval design guidelines")
    fingerprint(folder)


def update(args):
    repo = Path(args.repo).resolve()
    dest = Path(args.destination).absolute()
    state_path = Path(args.state).absolute()
    state_path.parent.mkdir(parents=True, exist_ok=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with state_path.with_suffix(".lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        state = json.loads(state_path.read_text()) if state_path.exists() else {}
        now = time.time()
        if args.seed:
            if state or dest.exists() or dest.is_symlink():
                raise ValueError("Initial installation already exists")
        elif now - state.get("last_attempt", 0) < INTERVAL:
            return {"status": "skipped", "reason": "Seven-day interval has not elapsed"}
        if dest.is_symlink():
            raise ValueError("Destination is a symlink; preserve it")
        if dest.exists() and fingerprint(dest) != state.get("installed_hash"):
            raise ValueError("Installed skill has local edits or is unmanaged; preserve it")
        state["last_attempt"] = now
        save(state_path, state)
        revision = "local-seed"
        if not args.seed:
            git(repo, "fetch", "origin", "+refs/heads/main:refs/remotes/origin/main")
            revision = git(repo, "rev-parse", "origin/main").decode().strip()
            if not git(repo, "ls-tree", revision, f"{SOURCE}/SKILL.md").strip():
                return {"status": "waiting", "reason": "origin/main does not contain the skill", "revision": revision}
        with tempfile.TemporaryDirectory(prefix=".revops-stage-", dir=dest.parent) as temporary:
            stage = Path(temporary) / "skill"
            if args.seed:
                shutil.copytree(repo / SOURCE, stage, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            else:
                archive = git(repo, "archive", "--format=tar", revision, SOURCE)
                with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
                    stage.mkdir()
                    for member in bundle.getmembers():
                        path = Path(member.name)
                        if path.is_absolute() or ".." in path.parts:
                            raise ValueError("Unsafe archive path")
                        if member.isdir() and path in Path(SOURCE).parents:
                            continue
                        relative = path.relative_to(SOURCE)
                        target = stage / relative
                        if member.isdir():
                            target.mkdir(parents=True, exist_ok=True)
                        elif member.isfile():
                            target.parent.mkdir(parents=True, exist_ok=True)
                            with bundle.extractfile(member) as source:
                                target.write_bytes(source.read())
                        else:
                            raise ValueError("Unsupported archive entry")
            validate(stage)
            new_hash = fingerprint(stage)
            changed = not dest.exists() or new_hash != state.get("installed_hash")
            if changed:
                backup = Path(temporary) / "previous"
                if dest.exists():
                    dest.rename(backup)
                try:
                    stage.rename(dest)
                except Exception:
                    if backup.exists():
                        backup.rename(dest)
                    raise
            state.update(installed_hash=new_hash, installed_revision=revision)
            save(state_path, state)
        return {"status": "installed" if args.seed else "updated" if changed else "unchanged", "revision": revision}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--destination", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--seed", action="store_true", help="Install local files once before they are published")
    args = parser.parse_args()
    try:
        result = update(args)
    except Exception as error:
        print(json.dumps({"status": "error", "reason": str(error)}))
        return 1
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
