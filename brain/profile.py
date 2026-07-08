"""
===========================================
TimiFX AI User Profile Engine
Phase 13 - Long Term Memory System
Author: Timilehin
===========================================
"""

import json
import os


PROFILE_FILE = "database/user_profile.json"



DEFAULT_PROFILE = {

    "name": "Timilehin",

    "project": "TimiFX AI",

    "role": "Founder",

    "goal": (
        "Build one of the world's best AI assistants "
        "using Python and modern AI technologies."
    ),

    "preferred_language": "English",

    "current_phase": "Phase 13",

    "preferences": {},

    "interests": {},

    "skills": {},

    "goals": {}

}



def load_profile():

    """
    Load user profile from storage.
    """

    if not os.path.exists(PROFILE_FILE):

        save_profile(
            DEFAULT_PROFILE
        )


    with open(
        PROFILE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)




def save_profile(profile):

    """
    Save user profile.
    """

    with open(
        PROFILE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            indent=4,
            ensure_ascii=False
        )



def update_profile(memory):

    """
    Merge extracted memory into profile.
    """

    profile = load_profile()


    for category, data in memory.items():

        if category not in profile:

            profile[category] = {}


        if isinstance(data, dict):

            profile[category].update(
                data
            )


    save_profile(profile)


    return profile




if __name__ == "__main__":


    test_memory = {

        "preferences": {

            "programming_language": "python"

        },

        "goals": {

            "current_interest":
            "Build AI tools"

        }

    }


    print(
        update_profile(
            test_memory
        )
    )