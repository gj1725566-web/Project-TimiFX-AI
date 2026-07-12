"""
===========================================
TimiFX AI Memory Analyzer
Phase 29.5

Responsible for:

- Detecting important information
- Filtering bad memories
- Classifying memories
- Assigning importance

Author: Timilehin
===========================================
"""


def analyze_memory(message):

    text = message.lower().strip()


    memory = {

        "content": message,

        "type": "temporary",

        "importance": 3

    }



    # ======================================
    # Ignore Questions
    # ======================================

    question_words = [

        "what",
        "why",
        "how",
        "when",
        "where",
        "who",
        "can you",
        "could you",
        "do you"

    ]


    for word in question_words:

        if text.startswith(word):

            return memory



    # ======================================
    # Ignore Commands
    # ======================================

    if any(symbol in text for symbol in [

        "+",
        "-",
        "*",
        "/"

    ]):

        return memory



    # ======================================
    # Long Term Memory Detection
    # ======================================

    important_keywords = [

        "my name is",

        "remember",

        "i like",

        "i love",

        "my favorite",

        "i prefer",

        "my project",

        "i work",

        "i am building"

    ]



    for keyword in important_keywords:


        if keyword in text:


            memory["type"] = "long_term"

            memory["importance"] = 8

            break



    return memory





# ===========================================
# TEST
# ===========================================

if __name__ == "__main__":


    tests = [

        "My name is Timilehin",

        "I love Python",

        "What do you remember about me?",

        "Calculate 50+50"

    ]


    for item in tests:

        print(
            analyze_memory(item)
        )