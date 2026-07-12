"""
===========================================
TimiFX AI Core Intelligence Engine
Phase 29 - Unified Memory Integration

Responsible for:

- Connecting Groq AI
- Loading Personality
- Using Unified Memory System
- Generating responses

Author: Timilehin
===========================================
"""


import os
import sys


# ===========================================
# Project Root
# ===========================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )



# ===========================================
# Imports
# ===========================================

from dotenv import load_dotenv

from groq import Groq


from brain.personality import (
    SYSTEM_PROMPT
)


from brain.memory_context import (
    build_memory_context
)



# ===========================================
# Load Environment
# ===========================================

load_dotenv()



# ===========================================
# Groq Client
# ===========================================

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)



# ===========================================
# Generate AI Response
# ===========================================

def generate_response(conversation):


    user_message = ""


    for item in conversation:

        if item["role"] == "user":

            user_message = item["content"]



    memory_context = build_memory_context(
        user_message
    )



    system_message = SYSTEM_PROMPT



    if memory_context:


        system_message += (

            "\n\n"

            +

            memory_context

        )



    messages = [


        {

            "role":
            "system",

            "content":
            system_message

        }


    ]



    messages.extend(
        conversation
    )



    response = client.chat.completions.create(

        model=
        "llama-3.3-70b-versatile",


        messages=
        messages,


        temperature=
        0.7

    )



    return (

        response

        .choices[0]

        .message

        .content

    )



# ===========================================
# Test
# ===========================================

if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Engine Test"
    )

    print("=" * 50)



    result = generate_response(

        [

            {

                "role":
                "user",

                "content":
                "What do you remember about me?"

            }

        ]

    )


    print()

    print(result)