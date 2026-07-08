"""
===========================================
TimiFX AI Backend v2.1

Backend + Memory Integration

Author: Timilehin
===========================================
"""


import sys
import os
from datetime import datetime


# Allow backend to access project folders
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from database.memory import (
    save_user,
    add_message,
    get_user
)


def start_ai(user_id, name, message):

    # Save user information
    save_user(
        user_id,
        name
    )

    # Store message in memory
    add_message(
        user_id,
        message
    )

    return {

        "project": "TimiFX AI",

        "status": "online",

        "user": get_user(
            user_id
        ),

        "response":
            "Message received and stored.",

        "time":
            str(datetime.now())

    }


if __name__ == "__main__":

    result = start_ai(

        1,

        "Timilehin",

        "Building TimiFX AI"

    )

    print(result)