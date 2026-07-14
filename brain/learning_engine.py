"""
===========================================
TimiFX AI Learning Engine
Phase 31

Responsible for:

- Learning from conversations
- Deciding what should be remembered
- Saving important memories
- Returning learning results

Author: Timilehin
===========================================
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )


from brain.memory_analyzer import analyze_memory
from brain.memory_manager import add_memory


# ===========================================
# Learn
# ===========================================

def learn(message):

    memory = analyze_memory(message)

    if memory["type"] == "long_term":

        result = add_memory(memory)

        return {

            "learned": True,

            "saved": result["saved"],

            "memory": result["memory"]

        }

    return {

        "learned": False,

        "saved": False,

        "memory": memory

    }


# ===========================================
# Test
# ===========================================

if __name__ == "__main__":

    print("=" * 50)
    print("TimiFX AI Learning Engine Test")
    print("=" * 50)

    tests = [

        "My name is Timilehin",

        "Remember I like Python",

        "Calculate 40+50",

        "I love Artificial Intelligence"

    ]

    for message in tests:

        print()

        print("Message:")

        print(message)

        print()

        print(
            learn(message)
        )