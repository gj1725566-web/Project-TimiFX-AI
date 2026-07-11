"""
===========================================
TimiFX AI Memory Search Engine
Phase 26

Responsible for:

- Searching memories
- Long-term memory retrieval
- Short-term memory retrieval
- Keyword matching
- Memory ranking

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
    LONG_TERM_FILE,
    SHORT_TERM_FILE
)


# ==========================================
# Search Memory
# ==========================================

def search_memory(query):

    query = query.lower()

    results = []

    # ------------------------------
    # Long Term Memory
    # ------------------------------

    long_term = load_memory(
        LONG_TERM_FILE
    )

    for memory in long_term["memories"]:

        content = memory.get(
            "content",
            ""
        )

        if query in content.lower():

            memory["source"] = (
                "long_term"
            )

            results.append(
                memory
            )

    # ------------------------------
    # Short Term Memory
    # ------------------------------

    short_term = load_memory(
        SHORT_TERM_FILE
    )

    for memory in short_term["memories"]:

        content = memory.get(
            "content",
            ""
        )

        if query in content.lower():

            memory["source"] = (
                "short_term"
            )

            results.append(
                memory
            )

    # ------------------------------
    # Sort by importance
    # ------------------------------

    results.sort(

        key=lambda x:
        x.get(
            "importance",
            0
        ),

        reverse=True

    )

    return results


# ==========================================
# Best Memory
# ==========================================

def get_best_memory(query):

    results = search_memory(
        query
    )

    if not results:

        return None

    return results[0]


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print(
        "TimiFX AI Memory Search Test"
    )
    print("=" * 50)

    results = search_memory(
        "Python"
    )

    print()

    print("Results:")

    print(results)

    print()

    print("Best Match:")

    print(
        get_best_memory(
            "Python"
        )
    )