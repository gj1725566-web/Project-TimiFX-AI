"""
===========================================
TimiFX AI Decision Engine
Author: Timilehin
Version: 1.0

Responsible for deciding which
intelligence systems should be used
for each user request.
===========================================
"""


def make_decision(reasoning, emotion, topic):

    decision = {

        "use_identity": False,

        "use_memory": False,

        "use_personality": True,

        "use_emotion": False,

        "use_conversation": True,

        "use_planner": False,

        "use_knowledge": False

    }


    intent = reasoning.get("intent", "general")


    # -----------------------------
    # Identity
    # -----------------------------

    if intent == "identity":

        decision["use_identity"] = True


    # -----------------------------
    # Memory
    # -----------------------------

    if reasoning.get("use_memory"):

        decision["use_memory"] = True


    # -----------------------------
    # Knowledge
    # -----------------------------

    if reasoning.get("use_knowledge"):

        decision["use_knowledge"] = True


    # -----------------------------
    # Emotion
    # -----------------------------

    if emotion["confidence"] == "high":

        decision["use_emotion"] = True


    # -----------------------------
    # Planner
    # -----------------------------

    if intent in [

        "programming",

        "general"

    ]:

        decision["use_planner"] = True


    # -----------------------------
    # Conversation

    # Always enabled

    # -----------------------------

    decision["topic"] = topic


    return decision


# ===========================================
# Test
# ===========================================

if __name__ == "__main__":

    print("=" * 50)

    print("TimiFX AI Decision Engine Test")

    print("=" * 50)

    reasoning = {

        "intent": "programming",

        "use_memory": True,

        "use_knowledge": True

    }

    emotion = {

        "emotion": "confused",

        "confidence": "high"

    }

    topic = "Python"

    result = make_decision(

        reasoning,

        emotion,

        topic

    )

    print()

    print(result)