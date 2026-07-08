"""
===========================================
TimiFX AI Intelligence Pipeline
Author: Timilehin
Version: 1.3

Connects:
- Reasoning Engine
- Planning Engine
- Conversation Memory
- Knowledge System
- Memory Extractor
- Context Manager
- User Profile Engine
- AI Engine
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

    sys.path.append(
        PROJECT_ROOT
    )



from brain.reasoning import analyze_intent

from brain.planner import create_plan

from brain.context_manager import (
    process_user_memory
)

from brain.profile import (
    load_profile
)

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





    # 2. Learn from message

    process_user_memory(
        user_message
    )



    # Reload updated profile

    profile = load_profile()






    # 3. Load conversation memory

    memory = []


    if reasoning["use_memory"]:

        memory = get_conversation_history(
            user_name
        )







    # 4. Load knowledge

    knowledge = {}


    if reasoning["use_knowledge"]:

        knowledge = get_knowledge()






    # 5. Create plan

    plan = None


    if reasoning["intent"] in [

        "programming",

        "general"

    ]:


        plan = create_plan(
            user_message
        )







    # 6. Build conversation

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







    # 7. Generate answer

    response = generate_response(
        conversation
    )







    return {


        "response":

            response,



        "reasoning":

            reasoning,



        "plan":

            plan,



        "knowledge":

            knowledge,



        "profile":

            profile,



        "memory_used":

            reasoning["use_memory"]

    }





if __name__ == "__main__":


    result = run_pipeline(

        "I love Python and I want to build AI tools"

    )


    print(result)