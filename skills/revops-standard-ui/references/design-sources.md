# Design sources

Read this reference when selecting patterns. These paths were checked on 2026-10-06. Inspect the current repository tree before use because paths and patterns can change.

## uselayouts

Repository: https://github.com/iurvish/uselayouts

Source locations:

- `content/docs/components/*.mdx`: component purpose and usage.
- `registry/default/example/*.tsx`: component implementation.
- `registry/default/demo/*-demo.tsx`: example integration.
- `registry/default/controls/*.json`: registry metadata and dependencies.
- `LICENSE`: current license and required notices.

The components use React, Motion, Tailwind CSS, and other dependencies. For standalone HTML, translate the selected behavior into semantic HTML, CSS, and plain JavaScript. Keep useful interaction details while adapting demo sizing and accessibility to the task.

Start with these candidates. Read the actual source before choosing one.

| Data or task | Candidate | What to assess |
| --- | --- | --- |
| Related dashboard sections | `bento-card` | Section navigation, hierarchy, and active state. Use full-sized content areas for real records. |
| Mutually exclusive views | `discrete-tabs` or `vertical-tabs` | Selected state and content switching. Keep labels visible when they are needed to identify views. |
| Filtering a record list | `filter-interaction` | Selected-option feedback and panel expansion. Connect selection to the actual records. |
| A list of records | `stacked-list` | Grouping and row emphasis. Keep tabular comparisons when columns matter. |
| A sequence of form steps | `multi-step-form` | Progress, validation, and retained input. |
| A field that users edit | `inline-edit` | Edit, save, cancel, and validation states. |

The component names are search entry points. They are not a fixed layout template. Inspect other components when they better fit the data.

## transitions.dev

Repository: https://github.com/Jakubantalik/transitions.dev

Source locations:

- `skills/transitions-dev/SKILL.md`: current transition index.
- `skills/transitions-dev/*.md`: transition instructions and snippets.
- `skills/transitions-dev/_root.css`: shared motion properties.
- `index.html`: live demonstrations and snippet templates.
- `LICENSE`: current use and redistribution terms.

Start with the transition that matches the state change.

| State change | Candidate source file | Purpose |
| --- | --- | --- |
| Record details open or close | `07-panel-reveal.md` | Show the relationship between summary and detail. |
| Active view changes | `16-tabs-sliding.md` | Track the selected view with a moving indicator. |
| Menu opens or closes | `05-menu-dropdown.md` | Anchor options to their trigger. |
| Dialog opens or closes | `06-modal.md` | Show a temporary task surface. |
| Section expands or collapses | `21-accordion.md` | Reveal secondary content within a group. |
| Operation completes | `22-toast.md` or `10-success-check.md` | Show confirmed feedback after an operation succeeds. |

For sliding tabs, the inspected source measures the active button position and width. It updates the indicator after initial layout and resize. Preserve that alignment behavior in an adaptation.

For panel reveal, the inspected source controls opacity, translation, and pointer events with an open-state attribute. Add focus and visibility management for closed content. Pointer-event rules alone do not remove content from keyboard navigation.

Read the selected transition's CSS, properties, and JavaScript orchestration. Keep its reduced-motion behavior. Adapt motion distance and duration to the real component size.

## Source lookup and attribution

Use a connected GitHub tool, web access, or a temporary read-only checkout. Inspect both catalogs first. Fetch only the candidate files needed for the task. Avoid adding either upstream repository to the user's project.

Record source URLs in this form when a commit SHA is available:

`https://github.com/<owner>/<repo>/blob/<commit-sha>/<path>`

Example source map:

| Output area | Data structure | Source pattern | Adaptation |
| --- | --- | --- | --- |
| Status filter | Mutually exclusive status values | uselayouts `filter-interaction` | Labeled buttons filter the actual records. |
| Record detail | One record with secondary fields | transitions.dev `07-panel-reveal.md` | Short reveal with focus management and reduced motion. |

Check the current license before copying source code. uselayouts currently uses MIT terms with notice requirements. transitions.dev currently permits use in products but restricts redistribution of its library as a competing collection. Link to those licenses rather than copying their catalogs into this skill. Use publicly available patterns by default.
