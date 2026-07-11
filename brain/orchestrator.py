"""
===========================================
TimiFX AI Master Orchestrator
Phase 25.6 - Full Brain Integration

Author: Timilehin
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



# ===============================
# IMPORT ENGINES
# ===============================


from brain.reasoning import (
    analyze_intent
)


from brain.emotional_response import (
    detect_emotion
)


from brain.conversation_engine import (
    update_conversation,
    get_conversation_summary
)


from brain.decision_engine import (
    make_decision
)


from brain.planner import (
    create_plan
)


from brain.tool_router import (
    route_tool
)



# ===============================
# AI RESPONSE ENGINE
# ===============================

try:

    from backend.ai_engine import (
        generate_response
    )

except Exception:


    def generate_response(messages):

        return (
            "TimiFX AI response engine is "
            "currently running in fallback mode."
        )





# ===============================
# MAIN THINK FUNCTION
# ===============================


def think(message):


    # ----------------------------
    # Reasoning
    # ----------------------------

    reasoning = analyze_intent(
        message
    )



    # ----------------------------
    # Emotion
    # ----------------------------

    emotion = detect_emotion(
        message
    )



    # ----------------------------
    # Conversation Memory
    # ----------------------------

    conversation = update_conversation(
        message
    )



    # ----------------------------
    # Decision Making
    # ----------------------------

    decision = make_decision(

        reasoning,

        emotion,

        conversation,

        message

    )



    # ----------------------------
    # Tool Execution
    # ----------------------------

    if decision.get(
        "use_tools"
    ):


        tool_result = route_tool(
            message
        )


        if tool_result.get(
            "success"
        ):


            return {

                "response":
                tool_result["result"],

                "tool_used":
                True,

                "tool":
                decision.get(
                    "tool"
                ),

                "decision":
                decision

            }




    # ----------------------------
    # Normal AI Response
    # ----------------------------


    response = generate_response(

        [

            {

                "role":
                "user",

                "content":
                message

            }

        ]

    )



    return {

        "response":
        response,


        "reasoning":
        reasoning,


        "emotion":
        emotion,


        "decision":
        decision,


        "plan":
        create_plan(
            message
        ),


        "conversation":
        conversation,


        "summary":
        get_conversation_summary()

    }





# ===============================
# TEST
# ===============================


if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Orchestrator Test"
    )

    print("=" * 50)



    tests = [

        "hello",

        "calculate 50+50",

        "I am excited to build the world's best AI assistant"

    ]



    for message in tests:


        print()

        print(
            "USER:",
            message
        )


        print()


        result = think(
            message
        )


        print(
            result
        )