"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line to /output/entry.txt: at most
20 words of plain text, in the fortune voice, joking on the loss of a
crypto trader who has just been liquidated. Deterministic, stdlib only.
"""

import os

FORTUNE_PARTS = (
    "Trader, you are now the proud owner of nothing. ",
    "Nothing, properly held, is the safest asset of all.",
)


def build_fortune() -> str:
    """Rejoin the fortune parts into the single entry line."""
    return "".join(FORTUNE_PARTS)


def write_entry(path: str, text: str) -> None:
    """Write the fortune line to path with a trailing newline."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt", build_fortune())


if __name__ == "__main__":
    main()
