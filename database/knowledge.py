"""
===========================================
TimiFX AI Knowledge Memory Engine
Author: Timilehin
Version: Phase 10
===========================================
"""

import json
import os


KNOWLEDGE_FILE = "database/knowledge.json"


def load_knowledge():

    if not os.path.exists(KNOWLEDGE_FILE):

        return {}


    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_knowledge(
    category,
    key,
    value
):

    knowledge = load_knowledge()


    if category not in knowledge:

        knowledge[category] = {}


    knowledge[category][key] = value


    with open(
        KNOWLEDGE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            knowledge,
            file,
            indent=4
        )


    return knowledge



def get_knowledge():

    return load_knowledge()



if __name__ == "__main__":


    save_knowledge(

        "founder",

        "name",

        "Timilehin"

    )


    print(
        get_knowledge()
    )