"""
===========================================
TimiFX AI Core Intelligence Engine
Phase 10 - Knowledge Memory Integration
Author: Timilehin
===========================================
"""


import os
import json

from dotenv import load_dotenv
from groq import Groq

from brain.personality import SYSTEM_PROMPT


# Load environment variables

load_dotenv()



# Groq Client

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



# Knowledge Memory File

KNOWLEDGE_FILE = "database/knowledge.json"



def load_knowledge():

    if not os.path.exists(
        KNOWLEDGE_FILE
    ):

        return {}


    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def build_memory_context():

    knowledge = load_knowledge()


    if not knowledge:

        return (
            "No important user knowledge stored yet."
        )


    context = """
Important information about the user:

"""


    for category, data in knowledge.items():

        context += f"\n{category.upper()}:\n"


        for key, value in data.items():

            context += (
                f"- {key}: {value}\n"
            )


    return context




def generate_response(conversation):


    memory_context = build_memory_context()



    messages = [

        {
            "role": "system",

            "content":
            SYSTEM_PROMPT
            +
            "\n\n"
            +
            memory_context

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


        temperature=0.7

    )



    return (

        response

        .choices[0]

        .message

        .content

    )