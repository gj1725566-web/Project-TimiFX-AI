"""
===========================================
TimiFX AI Intelligence Pipeline
Author: Timilehin
Version: 1.5

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
    # 3. Load identity
    # =====================================

    identity = get_identity()


    identity_context = identity_message()






    # =====================================
    # 4. Retrieve long-term memories
    # =====================================

    memory_context = get_memory_context(
        user_message
    )






    # =====================================
    # 5. Load conversation history
    # =====================================

    conversation_memory = []


    if reasoning["use_memory"]:

        conversation_memory = get_conversation_history(
            user_name
        )






    # =====================================
    # 6. Load knowledge
    # =====================================

    knowledge = {}


    if reasoning["use_knowledge"]:

        knowledge = get_knowledge()







    # =====================================
    # 7. Create plan
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
    # 8. Build AI context
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
    # 9. Generate response
    # =====================================

    response = generate_response(
        conversation
    )








    # =====================================
    # 10. Return intelligence package
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



        "memory_context":

            memory_context,



        "memory_used":

            reasoning["use_memory"]

    }









if __name__ == "__main__":


    result = run_pipeline(

        "Who are you?"

    )


    print(result)