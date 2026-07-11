"""
===========================================
TimiFX AI Memory Ranker
Phase 26

Ranks memory importance

Author: Timilehin
===========================================
"""


def rank_memory(memory):


    importance = memory.get(
        "importance",
        1
    )


    if importance >= 8:

        memory["priority"] = "high"


    elif importance >= 5:

        memory["priority"] = "medium"


    else:

        memory["priority"] = "low"



    return memory



if __name__ == "__main__":


    sample = {

        "content":"User likes Python",

        "importance":8

    }


    print(
        rank_memory(sample)
    )