"""
===========================================
TimiFX AI Memory Validator
Phase 14
Author: Timilehin
===========================================

Purpose:
Prevent useless or temporary information
from becoming long-term memory.
===========================================
"""

import re


QUESTION_STARTERS = [

    "what",
    "who",
    "where",
    "when",
    "why",
    "how",
    "which",
    "can",
    "could",
    "would",
    "should",
    "do",
    "does",
    "did",
    "is",
    "are",
    "am",
    "will"

]


TEMPORARY_WORDS = [

    "today",
    "yesterday",
    "tonight",
    "this morning",
    "this afternoon",
    "this evening",
    "right now",
    "currently"

]


def is_question(text):

    text = text.strip().lower()

    if text.endswith("?"):

        return True

    first_word = text.split()[0] if text.split() else ""

    return first_word in QUESTION_STARTERS


def is_temporary(text):

    text = text.lower()

    for word in TEMPORARY_WORDS:

        if word in text:

            return True

    return False


def validate_memory(message):

    """
    Returns

    {
        "valid": True/False,
        "reason": "..."
    }
    """

    message = message.strip()

    if len(message) < 8:

        return {

            "valid": False,

            "reason": "Message too short."

        }


    if is_question(message):

        return {

            "valid": False,

            "reason": "Questions should not become memory."

        }


    if is_temporary(message):

        return {

            "valid": False,

            "reason": "Temporary information."

        }


    return {

        "valid": True,

        "reason": "Long-term memory candidate."

    }


if __name__ == "__main__":

    tests = [

        "I love Python",

        "What do you know about me?",

        "I ate rice today",

        "I want to build AI tools",

        "How are you?"

    ]

    for test in tests:

        print("=" * 50)
        print(test)
        print(validate_memory(test))