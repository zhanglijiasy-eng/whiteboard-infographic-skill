# Whiteboard Infographic Style Guide

## Visual DNA

Use a clean Chinese hand-drawn whiteboard lesson style.

- Canvas: white or subtly warm white, wide margins, generous whitespace.
- Aspect: 3:2 landscape by default, often 1536 x 1024.
- Typography: large handwritten Chinese title; black marker body text; casual hand lettering for English terms such as `Agent`, `Skill`, `Prompt`.
- Palette: black and white first, red second. Avoid blue, green, orange, purple, gradients, and colorful social-card styling unless the user explicitly asks.
- Line work: thin black sketch lines, thin red outline boxes, red arrows, dashed red bands.
- Components: rounded rectangles, example boxes, thesis boxes, capability lists, icon rows, bottom takeaway lines.
- Icons: simple black/red line icons for document, folder, browser, database, computer, code, search, workflow, cloud, lock, robot, target, chart.
- Mood: educational, restrained, clear, like a course whiteboard rather than a poster template.

## Layout Recipes

### lesson-flow

Use for "what is X", product explanations, mechanisms, and cause/effect.

Structure:

1. Top-left title, optionally numbered.
2. Left example box.
3. Center thesis box with one red sentence.
4. Right capability or outcome box.
5. Middle or lower key mechanism box.
6. Bottom dashed icon band or final takeaway with a red keyword.

Prompt phrase:

`Use a sparse hand-drawn lesson-flow layout: left example box -> center thesis box -> right capability box, connected by thin red arrows, with a lower key-mechanism box and a bottom dashed icon band or final takeaway.`

### comparison

Use for A vs B, old way vs new way, chatbot vs agent.

Structure:

1. Two large side-by-side outline boxes.
2. Left side in black outline for the old/limited side.
3. Right side in red outline for the new/recommended side.
4. Center red arrow or small `VS`.
5. Bottom sentence states the practical takeaway.

Prompt phrase:

`Use a two-column comparison layout with black outline on the left, red outline on the right, a small red arrow or VS mark in the center, and a final takeaway line at the bottom.`

### capability-map

Use for systems, products, components, tools, or ability lists.

Structure:

1. Large title at top-left.
2. Central product/system box.
3. Surrounding capability boxes with icons.
4. Lower dashed band listing objects the system can touch or control.
5. Bottom conclusion sentence.

Prompt phrase:

`Use a capability-map layout with a central system box, surrounding black/red outline capability boxes, a lower dashed icon band, and one red-highlighted bottom conclusion.`

### dense-board

Use for long notes with many related ideas.

Structure:

1. Top-left title.
2. 4-6 compact outline cards in a grid.
3. Each card has a short label, one line icon, and 2-3 bullets.
4. Footer has one red-highlighted summary sentence.

Prompt phrase:

`Use a dense whiteboard layout: 4-6 compact black/red outline cards in a grid, each with a line icon and short bullets, plus a bottom summary sentence.`

## Anti-Patterns

Avoid:

- Photorealistic illustration.
- Dark backgrounds.
- Gradient blobs, bokeh, decorative orbs.
- Corporate SaaS dashboard UI.
- Filled colorful cards everywhere.
- Tiny Chinese text or long paragraphs.
- Random icons that do not map to text.
- Fake logos for products mentioned in the source.
- Copying any reference image verbatim.

## Image Prompt Template

```text
Create one Chinese teaching infographic in a minimal hand-drawn whiteboard lesson style.

Source idea:
{source_text}

Layout:
{layout_recipe}

Visual style:
White or warm-white 3:2 landscape canvas; large handwritten Chinese title at top-left; mostly black marker text; thin red and black rounded outline boxes; red arrows; red emphasis only for the core thesis; simple black/red line icons; dashed red bottom icon band or final takeaway; lots of whitespace; no gradients, no dark background, no colorful dashboard styling.

Content rules:
Compress the source into one title, 3-6 visual units, and one final takeaway. Use clear simplified Chinese. Keep text large and readable. Prefer short bullets over paragraphs. Preserve named products from the source. Do not add unrelated facts.

Output:
One polished infographic only, no surrounding explanation.
```
