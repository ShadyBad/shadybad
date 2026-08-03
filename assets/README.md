## Visual Asset Notes

- Generated via Python + Pillow (see `overlay_card.py`).
- Renders 1280×720 covers with a brand overlay and accent bar.
- GIFs are short (3–6s) loops to keep load <2.5 MB where possible.

### Brand tokens

- Background (ink): `#0D1117`
- Surface (card): `#0F172A`
- Text primary: `#E2E8F0`
- Text muted: `#94A3B8`
- Accent A (flow): `#14B8A6`
- Accent B (CTA): `#F59E0B`
- Border/lines: `#334155`

### Overlay script

Run:

```bash
python assets/overlay_card.py \
  --input assets/raw-capture.png \
  --title "Project — One-line subtitle" \
  --bullets "First point" "Second point" "Third point" \
  --output assets/project-demo.png
```

Optimize GIFs: `gifsicle --optimize=3 -o out.gif in.gif`
