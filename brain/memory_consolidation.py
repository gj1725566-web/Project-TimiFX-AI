"""
===========================================
TimiFX AI Memory Consolidation Engine
Phase 28

Responsible for:

- Removing duplicate memories
- Removing weak memories
- Keeping important memories
- Cleaning memory database

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


from brain.memory_manager import (
    load_memory,
    save_memory,
    LONG_TERM_FILE
)


MIN_IMPORTANCE = 5


# ==========================================
# Consolidate Memories
# ==========================================

def consolidate_memory():

    database = load_memory(
        LONG_TERM_FILE
    )

    memories = database.get(
        "memories",
        []
    )

    unique = {}

    for memory in memories:

        text = memory.get(
            "content",
            ""
        ).strip().lower()

        importance = memory.get(
            "importance",
            0
        )

        # Ignore weak memories
        if importance < MIN_IMPORTANCE:
            continue

        # Keep the highest importance version
        if text not in unique:

            unique[text] = memory

        else:

            if importance > unique[text].get(
                "importance",
                0
            ):

                unique[text] = memory

    database["memories"] = list(
        unique.values()
    )

    save_memory(
        LONG_TERM_FILE,
        database
    )

    return database["memories"]


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print(
        "TimiFX AI Memory Consolidation Test"
    )
    print("=" * 50)

    memories = consolidate_memory()

    print()

    print(
        f"Total Memories: {len(memories)}"
    )

    print()

    for memory in memories:

        print(memory)