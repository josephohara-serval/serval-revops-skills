# Serval design guidelines

Prepared October 6, 2026. Use these guidelines for the onboarding dashboard and related Serval materials.

## Basis and confidence

These guidelines combine observations from four supplied screenshots with the logo and color configuration on [Serval Documentation](https://docs.serval.com/). They are a working design reference. They are not an official, complete corporate brand manual.

- The documentation screenshots show dark navigation, purple selection indicators, white headings, gray body text, and blue information callouts.
- The product screenshot shows a neutral dark workspace, compact rows, gray navigation selection, white primary buttons, and purple labels.
- The official documentation configuration specifies primary purple `#845FF2` and light purple `#A99BF6`.
- Other colors below are sampled from screenshot pixels or recommended implementation values. Screenshot colors can differ from the original design tokens.
- Measurements are recommended CSS dimensions. The supplied screenshots were captured at high resolution. Do not treat screenshot pixels as CSS pixels.

## Logo

The Serval logo has a linked, diagonal ribbon-shaped symbol followed by the **Serval** wordmark. The symbol has two opposing curved sections with diagonal cuts. It is not a plain letter S or an animal illustration.

Use the official asset whenever a page or component features Serval branding. Use the full symbol-and-wordmark logo in the main navigation header. Use a symbol-only version only when an official symbol asset is available.

Verified assets are bundled with this skill:

- [White logo for dark surfaces](../assets/serval-logo-white.png)
- [Black logo for light surfaces](../assets/serval-logo-black.png)

Both assets are 2234 × 580 PNG files with transparency. Their aspect ratio is approximately 3.85:1. The dashboard embeds these files directly. It does not fetch them when opened.

Official asset sources:

- [White logo](https://mintcdn.com/serval/EZ4ObARAEFUZ9oeS/logo/dark.png)
- [Black logo](https://mintcdn.com/serval/EZ4ObARAEFUZ9oeS/logo/light.png)

### Logo rules

1. Preserve the full asset and its aspect ratio.
2. Use white on a dark surface.
3. Use black on a light surface or printed page.
4. Keep the logo upright.
5. Do not redraw the symbol or typeset a substitute wordmark.
6. Do not place the logo in a colored tile.
7. Do not add shadows, gradients, outlines, rotation, or animation to the logo.
8. Do not recolor the logo purple.
9. Keep clear space of at least half the displayed symbol height on each side. This is a working recommendation, not a verified corporate specification.
10. Use a full-logo height of approximately 28–32 CSS pixels in the dashboard sidebar. Use at least 24 pixels when space is limited.
11. Give the main logo the accessible name “Serval.” Keep duplicate decorative versions silent to screen readers.

A user avatar can contain initials. A workstream can use a functional icon. Neither is a substitute for the Serval logo.

## Color system

Use neutral dark surfaces as the base. Use purple for emphasis. Keep the logo white.

| Token | Value | Use | Evidence |
| --- | --- | --- | --- |
| `--serval-purple` | `#845FF2` | Primary brand accent | Official documentation configuration |
| `--serval-purple-light` | `#A99BF6` | Active text, links, focus, progress | Official documentation configuration |
| `--docs-background` | `#0C0C10` | Documentation-style dark canvas | Sampled from screenshots 1–3 |
| `--app-background` | `#151515` | Dashboard canvas | Sampled from screenshot 4 |
| `--sidebar-background` | `#111111` | Product sidebar | Sampled from screenshot 4 |
| `--surface` | `#1A1A1A` | Headers and shallow panels | Sampled from screenshot 4 |
| `--surface-raised` | `#262626` | Controls and tags | Sampled from screenshot 4 |
| `--border` | `#282828` | Dividers and outlines | Sampled from screenshot 4 |
| `--text-primary` | `#E2E1E5` | Titles and primary content | Sampled from documentation screenshots |
| `--text-secondary` | `#A2A1A5` | Body copy and navigation | Sampled from documentation screenshots |
| `--info-background` | `#151E3A` | Information callouts | Sampled from screenshots 1 and 3 |
| `--info-text` | `#9DC4F8` | Information text and icons | Sampled from screenshot 1 |

For implementation, use white `#FFFFFF` where stronger contrast is required. Use a subtle purple tint for selected filters. Use a neutral gray fill for selected product navigation. Use a purple line or text treatment for documentation-style navigation.

Keep semantic colors separate from brand colors. The product screenshot shows green for success and amber for active status or incidents. Do not use green as the dashboard’s main brand accent. Do not make an unreviewed action look like an error.

## Typography

Use Inter for interface text. The live documentation stylesheet declares Inter. The screenshots alone do not establish a corporate typeface for every Serval surface.

The dashboard embeds a local Inter Latin font. The skill includes [Inter Latin](../assets/inter-latin-variable.woff2) and its [license](../assets/INTER-LICENSE.txt). Use a system sans-serif fallback. Do not load remote fonts when the local file opens. Preserve the font license with the source assets.

Recommended sizes:

| Element | CSS size | Weight |
| --- | --- | --- |
| Main heading | 30–36 px | 600 |
| Section heading | 20–24 px | 600 |
| Task title | 13–14 px | 600 |
| Body and navigation | 12–14 px | 400–500 |
| Metadata and tags | 11–12 px | 400–500 |

Use sentence case for headings and controls. Reserve uppercase labels for short secondary metadata. Use moderate letter spacing. Keep paragraphs readable. Use bold text for important terms rather than decorative effects.

## Layout and components

- Keep a persistent left navigation area on desktop.
- Keep the main content aligned to a clear grid.
- Use a right rail for secondary information when space permits.
- Use thin borders and restrained surface differences.
- Keep table and task rows compact, with enough space for their text.
- Use modest corner radii: approximately 6–10 pixels for dashboard panels and controls.
- Use pill shapes for filters and short status labels.
- Make the selected navigation item clear with a neutral fill and readable text.
- Use purple for active filters, source links, and progress indicators.
- Use a white primary action with dark text when matching the product screenshot.
- Use simple outline icons with consistent stroke width.
- Avoid decorative gradients, glowing borders, heavy shadows, and tilted brand elements.

The dashboard can retain its uselayouts components. Apply the Serval colors and simple surface treatments to those components. Keep animation short and functional. Honor reduced-motion settings.

## Accessibility and behavior

Keep text contrast readable on dark surfaces. Use at least 4.5:1 contrast for normal text. Keep secondary text readable rather than fading it excessively.

Show a visible keyboard focus indicator. Keep control labels visible. Do not use color alone to show selection or review status. Pair the selected state with a fill, border, check, or text label.

Keep the review status distinct from task completion. Preserve all action descriptions, source references, filters, and saved review checks when changing appearance.

Use the black logo for printing. Remove dark backgrounds from the print layout. Keep the content readable without color printing.

## Screenshot references

1. **CleanShot 2026-10-06 at 12.08.20 AM@2x.png** — Team settings documentation. Shows the white logo, sidebar, active purple indicators, data table, and blue information callout.
2. **CleanShot 2026-10-06 at 12.07.58 AM@2x.png** — Data flow diagrams documentation. Shows heading hierarchy, spacing, and secondary diagram colors.
3. **CleanShot 2026-10-06 at 12.07.42 AM@2x.png** — Organization settings documentation. Shows purple category labels, body copy, headings, and blue callout treatment. The word “Branding” in the page navigation is product content; it does not supply a corporate brand manual.
4. **CleanShot 2026-10-06 at 12.09.51 AM@2x.png** — Serval ticket workspace. Shows neutral dark surfaces, a gray selected navigation row, compact filters, white primary action, purple labels, and semantic status colors.
