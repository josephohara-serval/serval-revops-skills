"""Regression checks for managed skill installation and updates."""

from argparse import Namespace
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import update_installation as updater


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="revops-update-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.origin = self.root / "origin"
        self.git("init", "-b", "main", str(self.origin))
        self.git("config", "user.name", "Fixture", repo=self.origin)
        self.git("config", "user.email", "fixture@example.invalid", repo=self.origin)
        self.source = self.origin / updater.SOURCE
        (self.source / "references").mkdir(parents=True)
        (self.source / "SKILL.md").write_text(
            "---\nname: revops-standard-ui\ndescription: Test fixture\n---\nBody\n"
        )
        (self.source / "references/serval-design.md").write_text("Design fixture")
        (self.source / "version.txt").write_text("old")
        self.commit()
        self.repo = self.root / "repo"
        self.git("clone", str(self.origin), str(self.repo))
        self.dest = self.root / "installed"
        self.state = self.root / "state.json"
        self.args = Namespace(
            repo=str(self.repo), destination=str(self.dest), state=str(self.state), seed=True
        )

    def git(self, *args, repo=None):
        command = ["git"]
        if repo is not None:
            command.extend(["-C", str(repo)])
        return subprocess.check_output(command + list(args), stderr=subprocess.PIPE)

    def commit(self):
        self.git("add", "-A", repo=self.origin)
        self.git("commit", "-m", "Fixture", repo=self.origin)

    def seed(self):
        result = updater.update(self.args)
        self.assertEqual(result["status"], "installed")
        self.args.seed = False

    def due(self):
        # Simulate a later weekly run without changing the saved state.
        last_attempt = json.loads(self.state.read_text())["last_attempt"]
        return patch.object(updater.time, "time", return_value=last_attempt + updater.INTERVAL + 1)

    def fail_install_state_save(self, error=OSError):
        original_save = updater.save
        calls = 0

        def save(path, state):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise error("State save failed")
            original_save(path, state)

        return patch.object(updater, "save", side_effect=save)

    def test_retry_seed_after_validation_failure(self):
        guide = self.repo / updater.SOURCE / "references/serval-design.md"
        guide.unlink()
        with self.assertRaisesRegex(ValueError, "Missing Serval"):
            updater.update(self.args)
        self.assertFalse(self.dest.exists())
        guide.write_text("Design fixture")
        self.seed()

    def test_failed_seed_state_save_removes_incomplete_install(self):
        with self.fail_install_state_save(), self.assertRaises(OSError):
            updater.update(self.args)
        self.assertFalse(self.dest.exists())
        self.assertNotIn("installed_hash", json.loads(self.state.read_text()))
        self.seed()

    def test_update_state_failure_restores_files_and_hash(self):
        self.seed()
        old_hash = updater.fingerprint(self.dest)
        (self.source / "version.txt").write_text("new")
        self.commit()
        with self.due(), self.fail_install_state_save(), self.assertRaises(OSError):
            updater.update(self.args)
        self.assertEqual((self.dest / "version.txt").read_text(), "old")
        self.assertEqual(updater.fingerprint(self.dest), old_hash)
        self.assertEqual(json.loads(self.state.read_text())["installed_hash"], old_hash)
        with self.due():
            self.assertEqual(updater.update(self.args)["status"], "updated")
        self.assertEqual((self.dest / "version.txt").read_text(), "new")

    def test_cancelled_update_restores_previous_installation(self):
        self.seed()
        (self.source / "version.txt").write_text("new")
        self.commit()
        with self.due(), self.fail_install_state_save(KeyboardInterrupt), self.assertRaises(KeyboardInterrupt):
            updater.update(self.args)
        self.assertEqual((self.dest / "version.txt").read_text(), "old")
        self.assertEqual(updater.fingerprint(self.dest), json.loads(self.state.read_text())["installed_hash"])

    def test_installed_seed_cannot_be_repeated(self):
        self.seed()
        self.args.seed = True
        with self.assertRaisesRegex(ValueError, "already exists"):
            updater.update(self.args)

    def test_interval_skips_remote_access(self):
        self.seed()
        with patch.object(updater, "git", side_effect=AssertionError("Unexpected fetch")):
            self.assertEqual(updater.update(self.args)["status"], "skipped")

    def test_installed_local_edits_are_preserved(self):
        self.seed()
        (self.dest / "version.txt").write_text("local")
        with self.due(), self.assertRaisesRegex(ValueError, "local edits"):
            updater.update(self.args)
        self.assertEqual((self.dest / "version.txt").read_text(), "local")

    def test_update_removes_files_deleted_upstream(self):
        self.seed()
        (self.source / "version.txt").unlink()
        self.commit()
        with self.due():
            self.assertEqual(updater.update(self.args)["status"], "updated")
        self.assertFalse((self.dest / "version.txt").exists())


if __name__ == "__main__":
    unittest.main()
