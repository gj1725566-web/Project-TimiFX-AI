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

import os
import sys

# ===========================================
# Add project root
# ===========================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# ===========================================
# Imports
# ===========================================

from brain.emotion_engine import (
    detect_emotion,
    emotion_instruction
)

# ===========================================
# Generate Emotional Guidance
# ===========================================

def generate_emotional_guidance(message):
    """
    Analyze the user's emotion and return
    guidance for the AI.
    """

    emotion_data = detect_emotion(message)

    instruction = emotion_instruction(
        emotion_data
    )

    return {

        "emotion": emotion_data,

        "response_guidance": instruction

    }


# ===========================================
# Backward Compatibility
# ===========================================

def build_emotional_context(message):
    """
    Older modules (such as the orchestrator)
    expect this function.

    It simply wraps
    generate_emotional_guidance().
    """

    return generate_emotional_guidance(
        message
    )


# ===========================================
# Apply Emotional Style
# ===========================================

def apply_emotional_style(
    response,
    message
):
    """
    Modify the AI response based on the
    detected user emotion.
    """

    emotion_data = detect_emotion(message)

    emotion = emotion_data.get(
        "emotion",
        "neutral"
    )

    if emotion == "happy":

        return (
            "😊 I'm glad to hear that!\n\n"
            + response
        )

    elif emotion == "sad":

        return (
            "I'm sorry you're feeling that way.\n"
            "I'm here to help.\n\n"
            + response
        )

    elif emotion == "frustrated":

        return (
            "I understand this can be frustrating.\n"
            "Let's solve it step by step.\n\n"
            + response
        )

    elif emotion == "confused":

        return (
            "No problem.\n"
            "I'll explain everything clearly "
            "step by step.\n\n"
            + response
        )

    return response


# ===========================================
# Test
# ===========================================

if __name__ == "__main__":

    print("=" * 50)
    print("TimiFX AI Emotional Response Engine Test")
    print("=" * 50)

    test_messages = [

        "I am excited about this AI project",

        "I feel sad today",

        "I am confused about Python",

        "This project is frustrating",

        "Hello"

    ]

    for message in test_messages:

        result = build_emotional_context(
            message
        )

        print()

        print("Message:")
        print(message)

        print()

        print(result)

        print("-" * 50)