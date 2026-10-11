#!/usr/bin/env python3
"""Regenerate the dimension/rank vector plot from the complete integer table."""

import argparse
import csv
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.table.open(newline="") as file:
        rows = list(csv.DictReader(file))
    width, height = 820, 430
    left, top, right, bottom = 80, 80, 780, 365
    xmax = max(int(r["order"]) for r in rows)
    ymax = max(int(r["dimension"]) for r in rows)

    def x(n):
        return left + (right - left) * (n - 1) / (xmax - 1)

    def y(v):
        return bottom - (bottom - top) * math.log10(v) / math.log10(ymax)

    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<g font-family="sans-serif" font-size="15" fill="#222">',
        '<text x="80" y="30" font-size="20">Exact dimensions and modular ranks through order 18</text>',
        '<text x="80" y="56">Blue line: source dimension; orange circles: rank mod 1000003</text>',
        '<text x="330" y="412">Original A,B letter count (order)</text>',
        '<text transform="translate(22,290) rotate(-90)">Dimension / rank (logarithmic scale)</text>',
    ]
    for value in (1, 10, 100, 1000):
        yy = y(value)
        pieces += [
            f'<line x1="{left}" y1="{yy:.2f}" x2="{right}" y2="{yy:.2f}" stroke="#ddd"/>',
            f'<text x="{left - 12}" y="{yy + 5:.2f}" text-anchor="end">{value}</text>',
        ]
    pieces.append(f'<path d="M {left} {top} V {bottom} H {right}" fill="none" stroke="#333"/>')
    for n in (1, 4, 8, 12, 16, 18):
        if n <= xmax:
            pieces.append(f'<text x="{x(n):.2f}" y="{bottom + 25}" text-anchor="middle">{n}</text>')
    points = " ".join(f"{x(int(r['order'])):.2f},{y(int(r['dimension'])):.2f}" for r in rows)
    pieces.append(f'<polyline points="{points}" fill="none" stroke="#2166ac" stroke-width="2"/>')
    for r in rows:
        pieces.append(
            f'<circle cx="{x(int(r["order"])):.2f}" cy="{y(int(r["rank"])):.2f}" r="4" fill="white" stroke="#d95f02" stroke-width="2"/>'
        )
    pieces += ["</g></svg>"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
