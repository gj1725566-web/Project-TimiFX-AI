"""
===========================================
TimiFX AI Decision Engine
Phase 25.3 - Intelligence Routing Layer

Responsible for deciding:

- Memory usage
- Knowledge usage
- Emotion usage
- Planning
- Tool execution

Author: Timilehin
===========================================
"""


def detect_tool_need(message):

    text = message.lower()


    # Calculator

    if any(word in text for word in [

        "calculate",
        "calculator",
        "+",
        "-",
        "*",
        "/"

    ]):

        return {

            "needed": True,

            "tool": "calculator"

        }



    # Greeting tool

    if any(word in text for word in [

        "hello",
        "hi",
        "hey"

    ]):

        return {

            "needed": True,

            "tool": "hello"

        }



    return {

        "needed": False,

        "tool": None

    }





def make_decision(

    reasoning,

    emotion,

    topic,

    message=""

):


    decision = {


        "use_identity": False,

        "use_memory": False,

        "use_personality": True,

        "use_emotion": False,

        "use_conversation": True,

        "use_planner": False,

        "use_knowledge": False,


        "use_tools": False,

        "tool": None

    }



    intent = reasoning.get(

        "intent",

        "general"

    )



    # Identity

    if intent == "identity":

        decision["use_identity"] = True



    # Memory

    if reasoning.get(

        "use_memory"

    ):

        decision["use_memory"] = True



    # Knowledge

    if reasoning.get(

        "use_knowledge"

    ):

        decision["use_knowledge"] = True



    # Emotion

    if emotion.get(

        "confidence"

    ) == "high":

        decision["use_emotion"] = True



    # Planner

    if intent in [

        "programming",

        "general"

    ]:

        decision["use_planner"] = True



    # Tools

    tool_result = detect_tool_need(

        message

    )


    if tool_result["needed"]:


        decision["use_tools"] = True


        decision["tool"] = tool_result["tool"]



    decision["topic"] = topic



    return decision





# ===========================================
# Test
# ===========================================


if __name__ == "__main__":


    reasoning = {


        "intent": "math",

        "use_memory": False,

        "use_knowledge": False

    }


    emotion = {


        "emotion": "neutral",

        "confidence": "low"

    }



    print(

        make_decision(

            reasoning,

            emotion,

            "Mathematics",

            "calculate 50+50"

        )

    )