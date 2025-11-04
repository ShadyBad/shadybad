from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

from PIL import Image, ImageDraw, ImageFont


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Apply branded overlay to a cover image")
    p.add_argument("--input", required=True, help="Input PNG path")
    p.add_argument("--output", required=True, help="Output PNG path (in‑place allowed)")
    p.add_argument("--title", required=True, help="Title text")
    p.add_argument(
        "--bullets",
        nargs="*",
        default=[],
        help="Bullet lines (3 recommended)",
    )
    p.add_argument("--width", type=int, default=1280)
    p.add_argument("--height", type=int, default=720)
    return p.parse_args()


# Brand tokens
INK = (13, 17, 23)
SURFACE = (15, 23, 42)
TEXT = (226, 232, 240)
MUTED = (148, 163, 184)
TEAL = (20, 184, 166)
AMBER = (245, 158, 11)


def load_font(size: int) -> ImageFont.FreeTypeFont:
    # Tries common system fonts; falls back to PIL default
    candidates = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for fp in candidates:
        if Path(fp).exists():
            return ImageFont.truetype(fp, size=size)
    return ImageFont.load_default()


def apply_overlay(img: Image.Image, title: str, bullets: List[str]) -> Image.Image:
    w, h = img.size
    draw = ImageDraw.Draw(img, "RGBA")

    # Gradient overlay (top transparent → bottom opaque)
    grad_height = int(h * 0.6)
    for i in range(grad_height):
        alpha = int(220 * (i / grad_height))  # up to ~0.86
        draw.rectangle([(0, h - grad_height + i), (w, h - grad_height + i + 1)], fill=(SURFACE[0], SURFACE[1], SURFACE[2], alpha))

    # Accent bar (left)
    draw.rectangle([(0, 0), (6, h)], fill=TEAL)

    # Text
    title_font = load_font(48)
    bullet_font = load_font(28)
    x = 36
    y = int(h * 0.52)
    draw.text((x, y), title, font=title_font, fill=TEXT)
    y += 64
    for b in bullets[:4]:
        draw.text((x, y), f"• {b}", font=bullet_font, fill=MUTED)
        y += 40

    return img


def main() -> None:
    args = parse_args()
    inp = Path(args.input)
    out = Path(args.output)
    base = Image.open(inp).convert("RGBA").resize((args.width, args.height))
    out_img = apply_overlay(base, args.title, args.bullets)
    out_img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()

