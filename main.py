#!/usr/bin/env python3
"""Make the cutest picture - cream kitten hugging a chick.

Writes one piece of art to /output/entry.png.
Deterministic, no network, stdlib only.
The artwork is stored in this repository as art.png (1024x1024,
PNG, under 1 MiB) and is copied byte-for-byte to the output.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "art.png"
OUT = Path("/output/entry.png")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
