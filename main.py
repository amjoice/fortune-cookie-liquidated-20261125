"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line to /output/entry.txt: at most
20 words of plain text, in the fortune voice, joking on the loss of a
crypto trader who has just been liquidated. Deterministic, stdlib only.
"""

import os

FORTUNE = (
    "Trader, you are now the proud owner of nothing. "
    "Nothing, properly held, is the safest asset of all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
