"""
===========================================
TimiFX AI Memory Retriever Engine
Phase 14 - Long Term Memory System
Author: Timilehin
===========================================

Purpose:
Search stored memories and return useful
information for the AI brain.
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



from database.memory import (
    get_conversation_history
)


from brain.profile import (
    load_profile
)




def search_memory(
    query,
    user_name="Timilehin"
):

    """
    Search user's stored memories.
    """

    query = query.lower()


    results = []


    # 1. Search conversation history

    conversations = get_conversation_history(
        user_name
    )


    for item in conversations:

        content = item.get(
            "content",
            ""
        )


        if query in content.lower():

            results.append(
                {
                    "type": "conversation",
                    "content": content
                }
            )



    # 2. Search user profile

    profile = load_profile()


    profile_text = str(
        profile
    ).lower()



    for word in query.split():

        if word in profile_text:

            results.append(
                {
                    "type": "profile",
                    "content": profile
                }
            )

            break



    return results





def get_memory_context(
    query
):

    """
    Convert memories into AI readable context.
    """


    memories = search_memory(
        query
    )


    if not memories:

        return (
            "No previous memory found."
        )



    context = """

Relevant previous memories:

"""


    for memory in memories:


        context += (
            f"\n- {memory}\n"
        )


    return context





if __name__ == "__main__":


    result = search_memory(
        "Python"
    )


    print(result)