---
name: revops-standard-ui
description: Build new HTML interfaces or redesign existing HTML files for RevOps workflows. Apply Serval design guidelines and match layouts to the underlying data, using uselayouts components and transitions.dev motion patterns as references.
---

# RevOps Standard UI

Create an HTML interface that helps a team read data and complete work. Read and apply [Serval design guidelines](references/serval-design.md) for every new file and redesign. Use these two sources for layout and interaction decisions:

- [uselayouts](https://github.com/iurvish/uselayouts): component composition and interaction patterns.
- [transitions.dev](https://github.com/Jakubantalik/transitions.dev): state transitions and motion.

Serval design guidelines take priority over the inspiration sources. Adapt source patterns to Serval colors, typography, logo rules, and component treatments. Treat the guide as a working design reference, with the evidence limits stated in the guide. Apply explicit user requirements when they override the guide.

## 1. Understand the data and task

For an existing HTML file, read the full file and its local CSS, JavaScript, and data dependencies. Identify records, fields, relationships, units, dates, groups, totals, and status values. Identify the user's main task and the controls that support it. Record the existing values, links, calculations, selectors, and event handlers that the redesign must preserve.

For a new file, use the supplied data and project brief. Identify the same data structure before choosing components. Ask for missing information only when it changes the task or the meaning of the data. Label sample data when the user requests a prototype. Keep unknown values explicit.

Write a short data-to-layout plan before implementation. Map each main data group to a component. State the purpose of each interaction. Infer the data structure from available inputs; HTML alone does not prove that a backend schema exists.

## 2. Inspect both design sources

Read [references/design-sources.md](references/design-sources.md) for source locations and selection guidance. Inspect the current catalog in both repositories. Read the source for candidates that fit the data-to-layout plan. A README or component name alone is not enough to implement a pattern.

Select patterns for their use in this task. Preserve comparison tables for records that users must compare. Use cards for summaries or independent groups. Use detail panels for secondary record information. Use motion to explain a change of state.

Keep a brief source map with the chosen component or transition, its source path, the commit SHA when available, and the reason it fits. Include at least one relevant pattern from each source when both have a useful match. If one source has no useful match, explain that decision. If a source is unavailable, use a verified local copy or state the limitation. Do not claim to have inspected unavailable source code.

## 3. Build or redesign the HTML

For a standalone HTML request, use semantic HTML, CSS, and plain JavaScript. Make the file open without a build step. Embed required styles and scripts by default. Adapt React and Motion patterns to browser APIs; React source and Tailwind classes do not run directly in a plain HTML file. Preserve the existing framework when the file belongs to an application.

For an existing file, edit the requested file unless the user asks for a separate output. Preserve data values, business rules, links, forms, and working controls. Update selectors and event handlers together when markup changes. Recalculate derived values from the original data. Keep each record available through the relevant view or filter.

For a new file, choose an output path from the request or project context. Build the main task before secondary decoration. Keep controls functional. Identify any prototype control that has no backend operation.

Apply the colors, typography, layout, and component rules in the Serval design guidelines. Use the bundled assets in `assets/` for the official logos and local Inter font. Embed these assets for a standalone file, or copy them into the application's asset directory. Keep output independent of the skill's installation path. Preserve the font license with the output assets. Use a system sans-serif fallback. Define reusable CSS custom properties from the guide's tokens. Keep operational data legible at normal zoom. Use text labels for status and units.

Use short, restrained transitions for selection, expansion, feedback, and navigation. Make data available without waiting for animation. Honor `prefers-reduced-motion` in CSS and JavaScript. Keep the final state and controls usable when motion is disabled.

Use native buttons and labeled inputs. Provide visible keyboard focus. Implement keyboard behavior for custom tabs, menus, and dialogs. Keep closed panels out of the focus order. Restore focus after a dialog closes. Make layouts usable on narrow screens and at 200% zoom. Keep wide comparison tables in a labeled scroll region when needed.

Apply only the selected source patterns. Follow their current licenses. Retain required notices when adapting source code. Keep source attribution in comments or a project notice. This skill links to the sources; it does not redistribute their component libraries.

## 4. Verify the result

Compare the output with the data inventory. Check record counts, values, totals, labels, units, links, and calculations. Exercise the main task and all changed controls. Check empty results and relevant error states.

Check the result against the Serval design guidelines. Verify logo aspect ratio and surface color, purple accents, neutral surfaces, typography, component treatments, text contrast, and print behavior. Confirm that bundled assets work from the output location.

When browser tools are available, open the file or application. Check desktop and narrow layouts, keyboard operation, reduced motion, and console errors. Fix failures within the task scope. If browser verification is unavailable, inspect the markup and scripts and report that visual and interaction checks remain unverified.

Return the output file link, the main changes, the source map, and the checks performed. State any remaining limitation. Keep the HTML as a local artifact unless the user requests publication.
