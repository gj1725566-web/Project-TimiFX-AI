"""
===========================================
TimiFX AI Memory Analyzer
Phase 26

Responsible for:
- Detecting important information
- Classifying memories
- Assigning memory type

Author: Timilehin
===========================================
"""


def analyze_memory(message):

    text = message.lower()


    memory = {

        "content": message,

        "type": "temporary",

        "importance": 3

    }


    important_keywords = [

        "my name is",
        "remember",
        "i like",
        "i love",
        "my favorite",
        "i prefer",
        "my project",
        "i work"

    ]


    for keyword in important_keywords:

        if keyword in text:

            memory["type"] = "long_term"

            memory["importance"] = 8

            break


    return memory



if __name__ == "__main__":


    tests = [

        "My name is Timilehin",

        "Calculate 50+50",

        "Remember I like Python"

    ]


    for item in tests:

        print(
            analyze_memory(item)
        )