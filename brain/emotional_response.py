"""
===========================================
TimiFX AI Emotional Response Engine
Phase 19 - Emotional Intelligence Layer

Connects:
- Emotion Detection
- Personality Engine
- Response Style Control

Author: Timilehin
===========================================
"""


import sys
import os


# Add project root

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)



from brain.emotion_engine import (
    detect_emotion,
    emotion_instruction
)





def generate_emotional_guidance(message):

    """
    Creates response guidance
    based on detected emotion.
    """


    emotion_data = detect_emotion(
        message
    )


    instruction = emotion_instruction(
        emotion_data
    )


    return {

        "emotion": emotion_data,

        "response_guidance": instruction

    }







def apply_emotional_style(response, message):

    """
    Adjust AI response style
    based on user's emotion.
    """


    emotion_data = detect_emotion(
        message
    )


    emotion = emotion_data["emotion"]



    if emotion == "happy":

        return (
            "😊 I'm glad to hear that!\n\n"
            + response
        )



    elif emotion == "sad":

        return (
            "I understand. "
            "I'm here to support you.\n\n"
            + response
        )



    elif emotion == "frustrated":

        return (
            "I understand this can be challenging. "
            "Let's solve it step by step.\n\n"
            + response
        )



    elif emotion == "confused":

        return (
            "No problem. I'll explain it clearly "
            "step by step.\n\n"
            + response
        )



    return response







if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Emotional Response Engine Test"
    )

    print("=" * 50)



    test_messages = [

        "I am excited about this AI project",

        "I feel sad today",

        "I am confused about Python",

        "This project is frustrating",

        "Hello"

    ]



    for message in test_messages:


        result = generate_emotional_guidance(
            message
        )


        print()

        print(
            "Message:",
            message
        )


        print(
            result
        )


        print("-" * 50)