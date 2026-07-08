"""
===========================================
TimiFX AI Reasoning Engine
Author: Timilehin
Version: 1.0
===========================================
"""


def analyze_intent(user_message):
    """
    Analyze the user's message and determine
    what kind of request it is.
    """

    message = user_message.lower()

    if any(word in message for word in [
        "code",
        "python",
        "program",
        "debug",
        "flask",
        "javascript",
        "html",
        "css",
        "git",
        "github"
    ]):

        return {
            "intent": "programming",
            "use_memory": True,
            "use_knowledge": True
        }

    elif any(word in message for word in [
        "who",
        "founder",
        "created",
        "creator",
        "your name"
    ]):

        return {
            "intent": "identity",
            "use_memory": False,
            "use_knowledge": True
        }

    elif any(word in message for word in [
        "remember",
        "previous",
        "before",
        "last time",
        "earlier"
    ]):

        return {
            "intent": "memory",
            "use_memory": True,
            "use_knowledge": False
        }

    elif any(word in message for word in [
        "calculate",
        "math",
        "+",
        "-",
        "*",
        "/"
    ]):

        return {
            "intent": "math",
            "use_memory": False,
            "use_knowledge": False
        }

    else:

        return {
            "intent": "general",
            "use_memory": True,
            "use_knowledge": True
        }


if __name__ == "__main__":

    test = analyze_intent(
        "Who created you?"
    )

    print(test)