"""
===========================================
TimiFX AI Memory Ranker
Phase 15 - Memory Importance Engine
Author: Timilehin
===========================================

Purpose:
Assign an importance score to memories so
the AI can retrieve the most valuable ones
first.
===========================================
"""


IMPORTANT_KEYWORDS = {

    "goal": 10,
    "dream": 10,
    "mission": 10,
    "founder": 10,
    "project": 9,
    "career": 9,
    "business": 9,

    "python": 8,
    "programming": 8,
    "ai": 8,
    "machine learning": 8,
    "deep learning": 8,

    "prefer": 7,
    "favorite": 7,
    "love": 7,
    "interest": 7,

    "learn": 6,
    "study": 6,
    "skill": 6,
    "experience": 6,

    "today": 1,
    "yesterday": 1,
    "breakfast": 1,
    "lunch": 1,
    "dinner": 1

}


def calculate_score(text):

    """
    Calculate importance score.
    """

    score = 0

    lower = text.lower()

    for keyword, value in IMPORTANT_KEYWORDS.items():

        if keyword in lower:

            score += value

    return score


def rank_memory(memories):

    """
    memories = list of strings

    returns ranked list
    """

    ranked = []

    for memory in memories:

        ranked.append({

            "memory": memory,

            "score": calculate_score(memory)

        })

    ranked.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return ranked


if __name__ == "__main__":

    samples = [

        "I want to build one of the world's best AI assistants.",

        "I love Python.",

        "I ate rice today.",

        "My project is called TimiFX AI.",

        "I enjoy programming."

    ]

    result = rank_memory(samples)

    for item in result:

        print(item)