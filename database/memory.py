import json
import os


MEMORY_FILE = "database/memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {}


    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_memory(name, message):

    memory = load_memory()


    if name not in memory:

        memory[name] = {
            "messages": []
        }


    memory[name]["messages"].append(
        message
    )


    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )


    return memory[name]



def get_memory(name):

    memory = load_memory()


    if name in memory:

        return memory[name]


    return {
        "messages": []
    }



if __name__ == "__main__":

    save_memory(
        "Timilehin",
        "Building TimiFX AI"
    )


    print(
        get_memory("Timilehin")
    )