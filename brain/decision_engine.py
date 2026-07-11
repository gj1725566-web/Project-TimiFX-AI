"""
===========================================
TimiFX AI Decision Engine
Phase 25 - Tool Intelligence Upgrade

Responsible for deciding which
intelligence systems should be used
for each user request.

Author: Timilehin
===========================================
"""


def make_decision(reasoning, emotion, topic):


    decision = {


        # Core intelligence

        "use_identity": False,

        "use_memory": False,

        "use_personality": True,

        "use_emotion": False,

        "use_conversation": True,

        "use_planner": False,

        "use_knowledge": False,


        # Tool Intelligence

        "use_tools": False

    }



    intent = reasoning.get(
        "intent",
        "general"
    )



    # =====================================
    # Identity
    # =====================================

    if intent == "identity":

        decision["use_identity"] = True



    # =====================================
    # Memory
    # =====================================

    if reasoning.get(
        "use_memory"
    ):

        decision["use_memory"] = True



    # =====================================
    # Knowledge
    # =====================================

    if reasoning.get(
        "use_knowledge"
    ):

        decision["use_knowledge"] = True



    # =====================================
    # Emotion
    # =====================================

    if emotion.get(
        "confidence"
    ) == "high":

        decision["use_emotion"] = True



    # =====================================
    # Planner
    # =====================================

    if intent in [

        "programming",

        "general"

    ]:

        decision["use_planner"] = True



    # =====================================
    # Tool Intelligence
    # =====================================

    if intent in [

        "math"

    ]:

        decision["use_tools"] = True



    # =====================================
    # Conversation
    # =====================================

    decision["topic"] = topic



    return decision





# ===========================================
# Test
# ===========================================

if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Decision Engine Test"
    )

    print("=" * 50)



    reasoning = {


        "intent": "math",

        "use_memory": False,

        "use_knowledge": False

    }



    emotion = {


        "emotion": "neutral",

        "confidence": "low"

    }



    topic = "Mathematics"



    result = make_decision(

        reasoning,

        emotion,

        topic

    )



    print()

    print(result)