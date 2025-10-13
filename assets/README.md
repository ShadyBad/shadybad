## Visual Asset Notes

- Generated on macOS using Python 3.9 + Pillow 11.3.0 (see `pip3 install --user pillow`).
- Script lives inline in README history (commit message will reference) and renders 1280×720 cards with rounded-corner overlays.
- Files produced:
  - `notioniq-demo.png` / `notioniq-demo.gif`
  - `ff-draft-tools-demo.png` / `ff-draft-tools-demo.gif`
  - `intrinsic-value-demo.png` / `intrinsic-value-demo.gif`
- Each GIF is a static loop of its PNG counterpart to keep load predictable while providing animated compatibility.
- Update workflow: tweak copy/colors in the script, re-run, replace assets, and verify optimized sizes with `gifsicle --optimize=3` if needed.
