"""
===========================================
TimiFX AI Context Manager
Phase 15 - Adaptive Memory Integration
Author: Timilehin
===========================================

Responsibilities:
- Filter user memory
- Extract useful information
- Update user profile
- Ignore temporary information
===========================================
"""

import sys
import os


# Add project root to Python path

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )


from brain.memory_filter import filter_memory
from brain.memory_extractor import extract_memory
from brain.profile import (
    update_profile,
    load_profile
)


def process_user_memory(message):
    """
    Main long-term memory pipeline.
    """

    # -----------------------------
    # Step 1: Decide whether this
    # message should be remembered.
    # -----------------------------

    decision = filter_memory(message)

    if not decision["important"]:

        return load_profile()

    # -----------------------------
    # Step 2: Extract structured
    # memory from the message.
    # -----------------------------

    extracted_memory = extract_memory(message)

    if not extracted_memory:

        extracted_memory = decision["memory"]

    # -----------------------------
    # Step 3: Save into profile.
    # -----------------------------

    profile = update_profile(
        extracted_memory
    )

    return profile


if __name__ == "__main__":

    tests = [

        "I prefer Python for AI development",

        "I want to build AI tools",

        "I ate rice today"

    ]

    for test in tests:

        print("=" * 60)
        print("Message:")
        print(test)

        print("\nUpdated Profile:")

        print(
            process_user_memory(
                test
            )
        )