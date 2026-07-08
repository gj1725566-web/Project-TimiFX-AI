"""
===========================================
TimiFX AI Intelligence Pipeline
Author: Timilehin
Version: 1.1

Connects:
- Reasoning Engine
- Planning Engine
- Memory System
- Knowledge System
- AI Engine
===========================================
"""


import sys
import os


# Add project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )



from brain.reasoning import analyze_intent

from brain.planner import create_plan


from database.memory import (
    get_conversation_history
)


from database.knowledge import (
    get_knowledge
)


from backend.ai_engine import (
    generate_response
)




def run_pipeline(
    user_message,
    user_name="Timilehin"
):


    # 1. Understand request

    reasoning = analyze_intent(
        user_message
    )



    # 2. Load memory

    memory = []


    if reasoning["use_memory"]:

        memory = get_conversation_history(
            user_name
        )



    # 3. Load knowledge

    knowledge = {}


    if reasoning["use_knowledge"]:

        knowledge = get_knowledge()



    # 4. Create plan

    plan = None


    if reasoning["intent"] in [

        "programming",
        "general"

    ]:

        plan = create_plan(
            user_message
        )



    # 5. Build conversation

    conversation = []


    conversation.extend(
        memory
    )


    conversation.append(

        {

            "role": "user",

            "content": user_message

        }

    )



    # 6. Ask AI engine

    response = generate_response(
        conversation
    )



    return {

        "response": response,

        "reasoning": reasoning,

        "plan": plan,

        "knowledge": knowledge,

        "memory_used":
        reasoning["use_memory"]

    }




if __name__ == "__main__":


    result = run_pipeline(

        "Help me build a Telegram bot"

    )


    print(result)