"""
===========================================
TimiFX AI Engine
Author: Timilehin
Version: Phase 9
===========================================
"""

import os

from dotenv import load_dotenv
from groq import Groq

from brain.personality import SYSTEM_PROMPT
from brain.profile import FOUNDER_PROFILE


# Load environment variables
load_dotenv()


# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(conversation):
    """
    Generate an AI response using the
    conversation history.
    """

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "system",
            "content": f"""
Founder Information

Name: {FOUNDER_PROFILE['name']}

Role: {FOUNDER_PROFILE['role']}

Project: {FOUNDER_PROFILE['project']}

Mission:
{FOUNDER_PROFILE['goal']}

Always remember that you were created by this founder.

Be respectful.

Help the founder build TimiFX AI into one of the world's best AI assistants.
"""
        }

    ]

    # Add previous conversation
    messages.extend(conversation)

    # Generate response
    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=messages,

        temperature=0.7

    )

    return (

        response
        .choices[0]
        .message
        .content

    )