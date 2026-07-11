"""
===========================================
TimiFX AI Calculator Tool
Phase 23 - Built-in Calculator

Author: Timilehin
===========================================
"""

import ast
import operator


# Allowed operations
OPERATORS = {

    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg

}


def evaluate(node):

    """
    Safely evaluate mathematical expressions.
    """

    # Python 3.8+
    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid constant.")


    # Backward compatibility
    elif hasattr(ast, "Num") and isinstance(node, ast.Num):

        return node.n


    elif isinstance(node, ast.BinOp):

        left = evaluate(node.left)

        right = evaluate(node.right)

        op = OPERATORS[type(node.op)]

        return op(left, right)


    elif isinstance(node, ast.UnaryOp):

        operand = evaluate(node.operand)

        op = OPERATORS[type(node.op)]

        return op(operand)


    raise TypeError("Unsupported expression.")


def calculate(expression):

    """
    Calculate a mathematical expression safely.
    """

    try:

        tree = ast.parse(
            expression,
            mode="eval"
        )

        result = evaluate(tree.body)

        return {

            "success": True,

            "result": result

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }


# Tool entry point
def run(expression):

    return calculate(expression)


if __name__ == "__main__":

    print("=" * 50)
    print("TimiFX AI Calculator Tool Test")
    print("=" * 50)

    tests = [

        "5+5",

        "10*8",

        "100/4",

        "2**8",

        "(20+5)*4",

        "100%7",

        "-15+5"

    ]

    for exp in tests:

        print()
        print("Expression:")
        print(exp)

        result = calculate(exp)

        print()
        print("Result:")
        print(result)