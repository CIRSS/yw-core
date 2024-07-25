import ast
import sys


def yw_generator(raw: str) -> str:
    """
    Generate YesWorkflow Syntax from a raw Python code.
    """
    raw_ast = ast.parse(raw, mode="exec")

    return raw


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        raw = f.read()
    print(yw_generator(raw))
