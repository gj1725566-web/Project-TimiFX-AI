"""
===========================================
TimiFX AI Planner Engine
Author: Timilehin
Version: 1.0
===========================================
"""


def create_plan(message: str):

    text = message.lower()

    # Default plan
    plan = {
        "goal": message,
        "steps": []
    }

    if "build" in text:

        plan["steps"] = [
            "Understand the user's goal",
            "Break the project into smaller tasks",
            "Generate the required code",
            "Explain each step clearly",
            "Verify the solution"
        ]

    elif "learn" in text:

        plan["steps"] = [
            "Identify the topic",
            "Explain the fundamentals",
            "Give examples",
            "Test understanding",
            "Suggest next learning steps"
        ]

    elif "fix" in text:

        plan["steps"] = [
            "Understand the error",
            "Locate the source",
            "Provide the fix",
            "Explain why it happened",
            "Verify everything works"
        ]

    else:

        plan["steps"] = [
            "Understand the request",
            "Think carefully",
            "Generate the best answer"
        ]

    return plan


if __name__ == "__main__":

    print(create_plan(
        "Build an AI assistant"
    ))