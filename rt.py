#!/usr/bin/env python3
"""
Script name: extract_lines.py

Usage:
    python extract_lines.py /path/to/input.txt

What it does:
1. Prints the 3rd line of the file.
2. Then repeatedly:
   - skips 4 lines
   - prints the next (5th) line
3. Removes all '-' characters.
4. Collapses multiple spaces into a single space.
"""

import sys
import re
from pathlib import Path


def normalize_text(text: str) -> str:
    """Remove '-' and collapse multiple spaces into one."""
    text = text.replace("-", "")
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def process_file(file_path: Path):
    with file_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    index = 2  # 3rd line (0-based index)

    while index < len(lines):
        cleaned = normalize_text(lines[index])
        print(cleaned)
        index += 5  # skip 4 lines, take the next one


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_lines.py <path_to_text_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists() or not file_path.is_file():
        print(f"Error: '{file_path}' is not a valid file.")
        sys.exit(1)

    process_file(file_path)


if __name__ == "__main__":
    main()
