"""
===========================================
TimiFX AI Smart Memory Retrieval Engine
Phase 14.2 - Memory Ranking System
Author: Timilehin
===========================================

Features:
- Keyword extraction
- Memory searching
- Memory scoring
- Relevant memory ranking
===========================================
"""


import sys
import os
import re


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





def extract_keywords(text):

    """
    Extract important words from a message.
    """


    words = re.findall(
        r"\b[a-zA-Z]+\b",
        text.lower()
    )


    ignored_words = [

        "what",
        "who",
        "where",
        "when",
        "how",
        "do",
        "does",
        "is",
        "are",
        "my",
        "your",
        "the",
        "a",
        "an",
        "i",
        "you"

    ]


    keywords = [

        word

        for word in words

        if word not in ignored_words

    ]


    return keywords





def calculate_score(
    memory_text,
    keywords
):

    """
    Score memory relevance.
    """


    score = 0


    text = memory_text.lower()


    for keyword in keywords:


        if keyword in text:

            score += 1



    return score







def search_memory(
    query,
    user_name="Timilehin"
):


    keywords = extract_keywords(
        query
    )


    memories = []



    # Search conversation memory

    conversations = get_conversation_history(
        user_name
    )


    for item in conversations:


        content = item.get(
            "content",
            ""
        )


        score = calculate_score(

            content,

            keywords

        )


        if score > 0:


            memories.append(

                {

                    "type": "conversation",

                    "content": content,

                    "score": score

                }

            )






    # Search profile memory


    profile = load_profile()


    profile_text = str(
        profile
    )


    score = calculate_score(

        profile_text,

        keywords

    )


    if score > 0:


        memories.append(

            {

                "type": "profile",

                "content": profile,

                "score": score

            }

        )






    # Sort highest relevance first


    memories.sort(

        key=lambda x: x["score"],

        reverse=True

    )



    return memories






def get_memory_context(
    query
):


    memories = search_memory(
        query
    )



    if not memories:


        return (
            "No relevant memory found."
        )



    context = """

Relevant memories from previous interactions:

"""



    for memory in memories[:5]:


        context += (

            f"\nMemory type: {memory['type']}"

            f"\nRelevance score: {memory['score']}"

            f"\nInformation: {memory['content']}\n"

        )



    return context






if __name__ == "__main__":


    result = search_memory(

        "What programming language do I like?"

    )


    print(result)