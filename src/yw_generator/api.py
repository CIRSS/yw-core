import sys

import yw_generator as yw


def main() -> None:
    try:
        with open(sys.argv[1], "r") as f:
            raw = f.read()
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found")
        sys.exit(1)

    yw_syntax = yw.yw_generator(raw)
    print(yw_syntax)
