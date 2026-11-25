"""One Line, One Laugh - make.fun entry.

Writes a single funny line (<= 200 chars, no trailing newline) to
<MAKEFUN_OUTPUT_DIR>/entry.txt. The punchline lands in the last three
words: the ficus, having been loved, escalates to a custody filing.
"""

import os

LINE = "I told my houseplants I loved them. The ficus filed for custody."


def main() -> None:
    # Fail loudly rather than ever submitting a gate-invalid line.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry is {len(LINE)} chars, must be 1-200")
    if LINE != LINE.strip() or "\n" in LINE:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
