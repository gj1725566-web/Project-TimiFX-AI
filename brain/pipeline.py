"""
===========================================
TimiFX AI Intelligence Pipeline
Author: Timilehin
Version: 1.6

Connects:
- Reasoning Engine
- Planning Engine
- Conversation Memory
- Knowledge System
- Memory Extractor
- Context Manager
- User Profile Engine
- Long-Term Memory Retrieval
- Identity Engine
- Personality Engine
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
    sys.path.append(PROJECT_ROOT)





from brain.reasoning import analyze_intent


from brain.planner import create_plan


from brain.context_manager import (
    process_user_memory
)


from brain.profile import (
    load_profile
)


from brain.memory_retriever import (
    get_memory_context
)


from brain.identity import (
    get_identity,
    identity_message
)


from brain.personality_engine import (
    get_personality,
    personality_message
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


    # =====================================
    # 1. Understand intention
    # =====================================

    reasoning = analyze_intent(
        user_message
    )





    # =====================================
    # 2. Learn from user message
    # =====================================

    process_user_memory(
        user_message
    )


    profile = load_profile()





    # =====================================
    # 3. Load identity system
    # =====================================

    identity = get_identity()


    identity_context = identity_message()







    # =====================================
    # 4. Load personality system
    # =====================================

    personality = get_personality()


    personality_context = personality_message()







    # =====================================
    # 5. Retrieve memories
    # =====================================

    memory_context = get_memory_context(
        user_message
    )







    # =====================================
    # 6. Conversation history
    # =====================================

    conversation_memory = []


    if reasoning["use_memory"]:

        conversation_memory = get_conversation_history(
            user_name
        )








    # =====================================
    # 7. Knowledge system
    # =====================================

    knowledge = {}


    if reasoning["use_knowledge"]:

        knowledge = get_knowledge()







    # =====================================
    # 8. Planning system
    # =====================================

    plan = None


    if reasoning["intent"] in [

        "programming",

        "general"

    ]:


        plan = create_plan(
            user_message
        )









    # =====================================
    # 9. Build AI context
    # =====================================

    conversation = []



    conversation.extend(
        conversation_memory
    )






    conversation.append(

        {

            "role": "system",

            "content": identity_context

        }

    )







    conversation.append(

        {

            "role": "system",

            "content": personality_context

        }

    )







    conversation.append(

        {

            "role": "system",

            "content": memory_context

        }

    )








    conversation.append(

        {

            "role": "user",

            "content": user_message

        }

    )










    # =====================================
    # 10. Generate response
    # =====================================

    response = generate_response(
        conversation
    )









    # =====================================
    # 11. Return complete intelligence
    # =====================================

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



        "identity":

            identity,



        "personality":

            personality,



        "memory_context":

            memory_context,



        "memory_used":

            reasoning["use_memory"]

    }













if __name__ == "__main__":


    result = run_pipeline(

        "How should you behave?"

    )


    print(result)