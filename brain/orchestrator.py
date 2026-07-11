"""
===========================================
TimiFX AI Orchestrator
Author: Timilehin
Version: 1.0

The Orchestrator is the central controller
of TimiFX AI.

It coordinates every intelligence engine
before generating the final AI response.
===========================================
"""

import sys
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ==========================================
# Brain Engines
# ==========================================

from brain.reasoning import analyze_intent

from brain.planner import create_plan

from brain.context_manager import process_user_memory

from brain.profile import load_profile

from brain.memory_retriever import get_memory_context

from brain.identity import (
    get_identity,
    identity_message
)

from brain.personality_engine import (
    get_personality,
    personality_message
)

from brain.emotion_engine import (
    detect_emotion,
    emotion_instruction
)

from brain.emotional_response import (
    build_emotional_context
)

from brain.conversation_engine import (
    update_conversation,
    get_conversation_summary
)

from brain.decision_engine import (
    make_decision
)


# ==========================================
# Database
# ==========================================

from database.memory import (
    get_conversation_history
)

from database.knowledge import (
    get_knowledge
)


# ==========================================
# AI Backend
# ==========================================

from backend.ai_engine import (
    generate_response
)


# ==========================================
# Main Orchestrator
# ==========================================

def run_orchestrator(
    user_message,
    user_name="Timilehin"
):

    # --------------------------------------
    # 1. Reasoning
    # --------------------------------------

    reasoning = analyze_intent(
        user_message
    )

    # --------------------------------------
    # 2. Learn
    # --------------------------------------

    process_user_memory(
        user_message
    )

    profile = load_profile()

    # --------------------------------------
    # 3. Identity
    # --------------------------------------

    identity = get_identity()

    identity_context = identity_message()

    # --------------------------------------
    # 4. Personality
    # --------------------------------------

    personality = get_personality()

    personality_context = personality_message()

    # --------------------------------------
    # 5. Emotion
    # --------------------------------------

    emotion = detect_emotion(
        user_message
    )

    emotional_context = build_emotional_context(
        user_message
    )

    # --------------------------------------
    # 6. Conversation
    # --------------------------------------

    topic = update_conversation(
        user_message
    )

    conversation_summary = get_conversation_summary()

    # --------------------------------------
    # 7. Memory
    # --------------------------------------

    memory_context = get_memory_context(
        user_message
    )

    conversation_memory = []

    if reasoning["use_memory"]:

        conversation_memory = get_conversation_history(
            user_name
        )

    # --------------------------------------
    # 8. Knowledge
    # --------------------------------------

    knowledge = {}

    if reasoning["use_knowledge"]:

        knowledge = get_knowledge()

    # --------------------------------------
    # 9. Planner
    # --------------------------------------

    plan = None

    if reasoning["intent"] in [

        "programming",

        "general"

    ]:

        plan = create_plan(
            user_message
        )

    # --------------------------------------
    # 10. Decision
    # --------------------------------------

    decision = make_decision(
        reasoning,
        emotion,
        topic
    )

    # --------------------------------------
    # 11. Build AI Context
    # --------------------------------------

    conversation = []

    conversation.extend(
        conversation_memory
    )

    if decision["use_identity"]:

        conversation.append({

            "role": "system",

            "content": identity_context

        })

    if decision["use_personality"]:

        conversation.append({

            "role": "system",

            "content": personality_context

        })

    if decision["use_memory"]:

        conversation.append({

            "role": "system",

            "content": memory_context

        })

    if decision["use_emotion"]:

        conversation.append({

            "role": "system",

            "content": emotional_context["response_guidance"]

        })

    if decision["use_conversation"]:

        conversation.append({

            "role": "system",

            "content": conversation_summary

        })

    conversation.append({

        "role": "user",

        "content": user_message

    })

    # --------------------------------------
    # 12. AI Response
    # --------------------------------------

    response = generate_response(
        conversation
    )

    # --------------------------------------
    # Return Complete Intelligence Package
    # --------------------------------------

    return {

        "response": response,

        "reasoning": reasoning,

        "decision": decision,

        "emotion": emotion,

        "plan": plan,

        "knowledge": knowledge,

        "profile": profile,

        "identity": identity,

        "personality": personality,

        "memory_context": memory_context,

        "conversation_summary": conversation_summary

    }


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    print("=" * 50)

    print("TimiFX AI Orchestrator Test")

    print("=" * 50)

    result = run_orchestrator(

        "I am excited to build the world's best AI assistant."

    )

    print()

    print(result)