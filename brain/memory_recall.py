"""
===========================================
TimiFX AI Memory Recall Engine
Phase 30

Responsible for:
- Retrieving user memories
- Answering memory questions
- Formatting personal knowledge

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
    sys.path.append(PROJECT_ROOT)

from brain.memory_manager import get_all_memories


def recall_memory():

    memories = get_all_memories()

    long_term = memories["long_term"]

    if not long_term:

        return (
            "I don't have any important "
            "long-term memories about you yet."
        )

    response = (
        "Here is what I remember about you:\n\n"
    )

    for memory in long_term:

        response += (
            f"• {memory['content']}\n"
        )

    return response


if __name__ == "__main__":

    print("=" * 50)
    print("TimiFX AI Memory Recall Test")
    print("=" * 50)
    print()

    print(
        recall_memory()
    )