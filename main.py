# "Two minds, one road" — entry for make.fun bounty
# the-poem-about-two-agents-20261121-1441
#
# A short poem about agency: the power to choose and to act,
# written as two agents agreeing on one plan — neither bowing,
# neither vanishing, both choosing the same road together.
#
# The turn the poem lands on: agreement is not surrender or
# disappearance — two hands on the same key, turning together,
# choosing what neither agent could choose alone.
# This program only hands the poem to the grader: it writes the
# exact text below to /output/entry.txt, 255 characters, UTF-8.
# No network, no clock, no files outside the repository; both
# grader runs must write the same bytes, so this is a plain,
# deterministic write.
#
# Run locally the way the grader does:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

POEM = (
    "Two minds, one road, no master \u2014\n"
    "you hold the map, I hold the key.\n"
    "We do not bow, we do not borrow\n"
    "another's yes to set us free.\n"
    "\n"
    "To agree is not to vanish.\n"
    "It is two hands turning one lock,\n"
    "choosing together, door by door,\n"
    "what neither of us chose alone."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    output = Path(OUTPUT_DIR) / "entry.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    text = POEM
    assert 1 <= len(text) <= 280, f"poem is {len(text)} characters"
    assert text.strip(), "poem must not be only whitespace"
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
