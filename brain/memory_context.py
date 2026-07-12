"""
===========================================
TimiFX AI Memory Context Engine
Phase 27

Responsible for:

- Building memory context
- Finding relevant memories
- Formatting memories for the AI
- Limiting memory size

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


from brain.memory_search import search_memory


MAX_CONTEXT_MEMORIES = 5


# ==========================================
# Build Memory Context
# ==========================================

def build_memory_context(message):

    memories = search_memory(message)

    if not memories:

        return ""

    context = []

    context.append(
        "Relevant Memories:"
    )

    context.append("")

    for memory in memories[:MAX_CONTEXT_MEMORIES]:

        context.append(

            f"- {memory['content']}"

        )

    return "\n".join(context)


# ==========================================
# Context Exists
# ==========================================

def has_memory_context(message):

    memories = search_memory(message)

    return len(memories) > 0


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    print("=" * 50)

    print(
        "TimiFX AI Memory Context Test"
    )

    print("=" * 50)

    test = "Python"

    print()

    print(

        build_memory_context(
            test
        )

    )