"""
===========================================
TimiFX AI Memory System v2.0

Simple User Memory Foundation

Author: Timilehin
===========================================
"""


users = {}


def save_user(user_id, name):

    users[user_id] = {

        "name": name,

        "messages": []

    }


def add_message(user_id, message):

    if user_id in users:

        users[user_id]["messages"].append(message)


def get_user(user_id):

    return users.get(
        user_id,
        "User not found"
    )



if __name__ == "__main__":

    save_user(1, "Timilehin")

    add_message(
        1,
        "Building TimiFX AI"
    )

    print(get_user(1))