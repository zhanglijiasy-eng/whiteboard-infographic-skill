---
name: whiteboard-infographic
description: Generate Chinese hand-drawn whiteboard infographics from paragraphs, lesson notes, explainer text, product explanations, or slide-style content. Use when the user asks for a graphic, information diagram, teaching board, course visual, Xiaohongshu/Bilibili knowledge card, or specifically wants a minimal black-white-red handwritten whiteboard style with red outlines, arrows, line icons, and generous whitespace.
---

# Whiteboard Infographic

## Overview

Turn source text into a single polished Chinese teaching infographic that feels like a precise hand-drawn whiteboard lesson: white canvas, black marker text, red emphasis, thin red/black outline boxes, red arrows, simple line icons, and lots of breathing room.

Use image generation for the final artifact unless the user explicitly asks only for a prompt.

## Workflow

1. Read the user's source text and identify one teachable idea.
2. Compress the content into 3-6 visual units: examples, contrast, mechanism, capabilities, local context, conclusion.
3. Choose a layout from `references/style-guide.md`:
   - `lesson-flow` for explanation, cause/effect, or "what is X".
   - `comparison` for chatbot vs agent, old vs new, before vs after.
   - `capability-map` for products, systems, components, or lists of abilities.
   - `dense-board` for long notes that need 4-6 compact sections.
4. For longer text or repeated work, run `scripts/build_prompt.py` to create a stable image prompt.
5. Generate a 3:2 landscape image by default. Use portrait only when the user asks for a mobile poster or vertical social card.
6. Inspect the result for Chinese legibility, hierarchy, whitespace, and whether it stayed mostly black/white/red. Regenerate with fewer words if crowded.

## Prompt Requirements

Always include these constraints in the final image prompt:

- White or warm-white background, no dark hero background.
- 3:2 landscape teaching board, similar to 1536 x 1024, unless the user requests another size.
- Top-left large handwritten Chinese title, optionally numbered like `1、主题`.
- Mostly black marker text, with red used only for the key thesis, arrows, borders, and emphasis.
- Thin red and black rounded outline boxes; avoid filled cards unless a very light tint is necessary.
- Sparse modular layout with clear arrows, not a colorful dashboard.
- Simple black/red line icons tied to nouns in the text.
- Short Chinese phrases and bullets; no pasted paragraphs; no tiny text.

## Compression Rules

- Title: 6-16 Chinese characters, or a short Chinese-English mix.
- Subtitle: at most one short sentence.
- Section labels: 2-8 characters.
- Card body: 1-4 bullets, each preferably under 14 Chinese characters.
- Final takeaway: one memorable sentence, with the main phrase in red.
- Preserve named products from the source, but do not invent logos or unrelated brands.

## Quality Bar

The image should look like a clean course slide drawn by hand and polished digitally:

- The reading path is obvious in under 3 seconds.
- The canvas has visible whitespace.
- Red marks the thesis, not random decoration.
- Icons clarify meaning instead of filling space.
- The final line or bottom icon band makes the conclusion memorable.

## Resources

- Read `references/style-guide.md` for layout recipes and anti-patterns.
- Run `scripts/build_prompt.py` for a ready-to-use image prompt:

```bash
python3 scripts/build_prompt.py --text "你的输入文字"
python3 scripts/build_prompt.py --file input.txt --layout lesson-flow --orientation landscape
```
