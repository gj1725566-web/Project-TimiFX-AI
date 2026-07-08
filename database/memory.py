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




def save_conversation(
        name,
        role,
        content
):

    memory = load_memory()


    if name not in memory:

        memory[name] = {

            "conversation": []

        }



    memory[name]["conversation"].append(

        {

            "role": role,

            "content": content

        }

    )



    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            memory,

            file,

            indent=4,

            ensure_ascii=False

        )


    return memory[name]




def get_memory(name):

    memory = load_memory()


    if name in memory:

        return memory[name]


    return {

        "conversation": []

    }




def get_conversation_history(name):

    memory = get_memory(name)


    return memory.get(

        "conversation",

        []

    )




if __name__ == "__main__":


    save_conversation(

        "Timilehin",

        "user",

        "Building TimiFX AI"

    )


    print(

        get_memory("Timilehin")

    )