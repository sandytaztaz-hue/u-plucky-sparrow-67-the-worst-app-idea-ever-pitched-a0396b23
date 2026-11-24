"""One-sentence pitch entry for the make.fun Worst App Idea Ever Pitched competition.

The program writes one sentence to /output/entry.txt: a deadpan startup pitch
for PocketCheck, an app that texts your phone every morning to confirm your
phone is still in your pocket — and assumes you have lost your pocket if it
cannot reach your phone. One sentence, one idea, pitched with total founder
confidence: a problem nobody has, solved by the very device the problem is about.
"""

import os

LINE = "PocketCheck is a $3-a-month app that texts your phone every morning to confirm your phone is still in your pocket, and if it cannot reach your phone, it assumes you have lost your pocket."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
