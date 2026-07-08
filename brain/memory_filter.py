"""
===========================================
TimiFX AI Memory Filter Engine
Phase 15 - Adaptive Learning Brain
Author: Timilehin
===========================================

Purpose:
Decides what information is important enough
to store in long-term memory.

Important:
- Goals
- Preferences
- Skills
- Personal project information
- Long-term interests

Ignored:
- Temporary conversations
- Casual statements
===========================================
"""


import re



# Information categories worth remembering

IMPORTANT_PATTERNS = {

    "preferences": [

        "i like",
        "i love",
        "i prefer",
        "my favorite",
        "i use",
        "i enjoy"

    ],


    "goals": [

        "i want to",
        "i plan to",
        "my goal",
        "i am building",
        "i am creating",
        "i hope to"

    ],


    "skills": [

        "i know",
        "i learned",
        "i can",
        "i have experience"

    ],


    "interests": [

        "i am interested",
        "i enjoy",
        "i love learning",
        "i follow"

    ]

}





def clean_text(text):

    """
    Clean user message.
    """

    return text.lower().strip()





def detect_memory_type(message):

    """
    Detect what type of memory
    should be created.
    """


    text = clean_text(
        message
    )


    detected = {}



    for category, patterns in IMPORTANT_PATTERNS.items():


        for pattern in patterns:


            if pattern in text:


                detected[category] = text

                break



    return detected






def extract_memory_value(
    message
):

    """
    Extract useful information
    from the message.
    """


    text = message.strip()


    text = re.sub(

        r"^(i|my)\s+",

        "",

        text,

        flags=re.IGNORECASE

    )


    return text






def filter_memory(message):

    """
    Main memory decision engine.

    Returns:
    {
        important: True/False,
        memory: {...}
    }
    """



    memory_types = detect_memory_type(
        message
    )



    if not memory_types:


        return {

            "important": False,

            "memory": {}

        }





    memory = {}



    for category in memory_types:


        value = extract_memory_value(
            message
        )


        memory[category] = {


            "information": value

        }





    return {


        "important": True,


        "memory": memory

    }





if __name__ == "__main__":


    tests = [

        "I prefer Python for AI development",

        "I want to build AI tools",

        "I ate rice today"

    ]



    for test in tests:


        print(

            test,

            "\n",

            filter_memory(test),

            "\n"

        )