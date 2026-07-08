"""
===========================================
TimiFX AI Memory Extractor
Phase 13 - Long Term Memory System
Author: Timilehin
===========================================
"""

import re


def extract_memory(message):

    """
    Analyze user messages and extract
    useful long-term information.
    """

    memory = {}


    text = message.lower()



    # Detect programming preferences

    languages = [
        "python",
        "javascript",
        "java",
        "c++",
        "typescript"
    ]


    for language in languages:

        if language in text:

            memory.setdefault(
                "preferences",
                {}
            )

            memory["preferences"][
                "programming_language"
            ] = language

            break




    # Detect goals

    if "build" in text:

        memory.setdefault(
            "goals",
            {}
        )


        memory["goals"][
            "current_interest"
        ] = message




    # Detect likes

    match = re.search(
        r"i like (.+)",
        text
    )


    if match:

        memory.setdefault(
            "preferences",
            {}
        )


        memory["preferences"][
            "likes"
        ] = match.group(1)




    return memory




if __name__ == "__main__":


    test = extract_memory(
        "I like Python and I want to build AI tools"
    )


    print(test)