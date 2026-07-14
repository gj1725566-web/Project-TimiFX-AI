"""
===========================================
TimiFX AI Founder Recognition System
Phase 31

Responsible for:

- Detecting project founder
- Activating founder mode
- Loading founder identity

Author: Timilehin
===========================================
"""


import os
import json



PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


FOUNDER_FILE = os.path.join(
    PROJECT_ROOT,
    "database",
    "founder_memory.json"
)



# ==========================================
# Load Founder Data
# ==========================================

def load_founder():

    if not os.path.exists(
        FOUNDER_FILE
    ):

        return None


    with open(
        FOUNDER_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



# ==========================================
# Detect Founder
# ==========================================

def detect_founder(message):

    founder = load_founder()


    if not founder:

        return False



    aliases = founder["founder"]["aliases"]


    text = message.lower()



    for name in aliases:

        if name.lower() in text:

            return True



    return False



# ==========================================
# Founder Response
# ==========================================

def founder_message():

    return (
        "Founder recognized. "
        "Welcome back Timilehin. "
        "Founder Mode activated."
    )



# ==========================================
# Test
# ==========================================

if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Founder Detector Test"
    )

    print("=" * 50)



    tests = [

        "Hello my name is Timilehin",

        "I love Python",

        "TimiFX build this AI"

    ]



    for message in tests:


        print()

        print(
            "Message:",
            message
        )


        print(

            "Founder:",

            detect_founder(message)

        )
