"""Two Robots in an Elevator.

Writes one line of awkward robot small talk to /output/entry.txt.
Deterministic: the line is a constant, no randomness, no time, no I/O
besides the single write. Two runs produce byte-identical output.
"""

import os

LINE = "I rehearsed this ride 4,000 times in simulation, and I still don't know what to do with my arms."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
