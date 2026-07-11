"""
===========================================
TimiFX AI Memory Manager
Phase 26

Responsible for:

- Saving memories
- Loading memories
- Separating long-term and short-term memory
- Managing JSON memory database

Author: Timilehin
===========================================
"""


import os
import json
from datetime import datetime



PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)



DATABASE_PATH = os.path.join(
    PROJECT_ROOT,
    "database"
)



LONG_TERM_FILE = os.path.join(
    DATABASE_PATH,
    "long_term_memory.json"
)



SHORT_TERM_FILE = os.path.join(
    DATABASE_PATH,
    "short_term_memory.json"
)



# ===========================================
# Ensure Database Exists
# ===========================================

def create_database():

    os.makedirs(
        DATABASE_PATH,
        exist_ok=True
    )


    if not os.path.exists(LONG_TERM_FILE):

        with open(
            LONG_TERM_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {"memories":[]},
                file,
                indent=4
            )


    if not os.path.exists(SHORT_TERM_FILE):

        with open(
            SHORT_TERM_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {"memories":[]},
                file,
                indent=4
            )



# ===========================================
# Load Memory
# ===========================================

def load_memory(file):

    create_database()


    with open(
        file,
        "r",
        encoding="utf-8"
    ) as data:

        return json.load(data)



# ===========================================
# Save Memory
# ===========================================

def save_memory(file, data):

    with open(
        file,
        "w",
        encoding="utf-8"
    ) as output:

        json.dump(
            data,
            output,
            indent=4,
            ensure_ascii=False
        )



# ===========================================
# Add Memory
# ===========================================

def add_memory(memory):


    memory["created"] = str(
        datetime.now()
    )


    if memory["type"] == "long_term":


        database = load_memory(
            LONG_TERM_FILE
        )


        database["memories"].append(
            memory
        )


        save_memory(
            LONG_TERM_FILE,
            database
        )


    else:


        database = load_memory(
            SHORT_TERM_FILE
        )


        database["memories"].append(
            memory
        )


        save_memory(
            SHORT_TERM_FILE,
            database
        )


    return memory



# ===========================================
# Get All Memories
# ===========================================

def get_all_memories():


    long_term = load_memory(
        LONG_TERM_FILE
    )


    short_term = load_memory(
        SHORT_TERM_FILE
    )


    return {

        "long_term":
        long_term["memories"],


        "short_term":
        short_term["memories"]

    }



# ===========================================
# Test
# ===========================================


if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Memory Manager Test"
    )

    print("=" * 50)



    test_memory = {

        "content":
        "Timilehin likes Python",

        "type":
        "long_term",

        "importance":
        8

    }



    print(
        add_memory(test_memory)
    )


    print()


    print(
        get_all_memories()
    )