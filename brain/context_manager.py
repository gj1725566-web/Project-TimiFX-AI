"""
===========================================
TimiFX AI Context Manager
Phase 13 - Memory Integration Layer
Author: Timilehin
===========================================
"""

import sys
import os


# Add project root to Python path

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )



from brain.memory_extractor import extract_memory
from brain.profile import update_profile, load_profile




def process_user_memory(message):

    """
    Extract useful information
    and update user profile.
    """


    extracted_memory = extract_memory(
        message
    )


    if extracted_memory:

        profile = update_profile(
            extracted_memory
        )

        return profile



    return load_profile()




if __name__ == "__main__":


    result = process_user_memory(

        "I love Python and I want to build AI tools"

    )


    print(result)