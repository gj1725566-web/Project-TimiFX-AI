"""
===========================================
TimiFX AI Conversation Engine
Author: Timilehin
Version: 1.0

Responsible for:

- Topic Detection
- Topic Switching
- Conversation State
- Conversation Summary
- Conversation Reset
===========================================
"""

import json
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATABASE = os.path.join(
    PROJECT_ROOT,
    "database",
    "conversation_state.json"
)


DEFAULT_STATE = {

    "current_topic": "General",

    "previous_topic": "",

    "history": []

}


# ===========================================
# Load conversation state
# ===========================================

def load_state():

    if not os.path.exists(DATABASE):

        save_state(DEFAULT_STATE)

        return DEFAULT_STATE.copy()

    with open(DATABASE, "r", encoding="utf-8") as file:

        return json.load(file)


# ===========================================
# Save conversation state
# ===========================================

def save_state(state):

    with open(DATABASE, "w", encoding="utf-8") as file:

        json.dump(
            state,
            file,
            indent=4
        )


# ===========================================
# Detect Topic
# ===========================================

def detect_topic(message):

    text = message.lower()


    topics = {

        "Python": [

            "python",
            "coding",
            "programming",
            "script"

        ],

        "Artificial Intelligence": [

            "ai",
            "assistant",
            "chatbot",
            "machine learning",
            "llm"

        ],

        "Memory System": [

            "memory",
            "profile",
            "remember"

        ],

        "Git/GitHub": [

            "git",
            "github",
            "commit",
            "push",
            "branch"

        ],

        "Telegram Bot": [

            "telegram",
            "bot",
            "botfather"

        ],

        "Web Development": [

            "website",
            "flask",
            "fastapi",
            "api"

        ]

    }


    for topic, keywords in topics.items():

        for keyword in keywords:

            if keyword in text:

                return topic


    return "General"


# ===========================================
# Update State
# ===========================================

def update_conversation(message):

    state = load_state()

    detected = detect_topic(message)

    if detected != state["current_topic"]:

        state["previous_topic"] = state["current_topic"]

        state["current_topic"] = detected


    state["history"].append({

        "message": message,

        "topic": detected

    })


    if len(state["history"]) > 25:

        state["history"] = state["history"][-25:]


    save_state(state)

    return state


# ===========================================
# Current Topic
# ===========================================

def get_current_topic():

    return load_state()["current_topic"]


# ===========================================
# Previous Topic
# ===========================================

def get_previous_topic():

    return load_state()["previous_topic"]


# ===========================================
# Conversation Summary
# ===========================================

def get_summary():

    state = load_state()

    lines = []

    lines.append(

        f"Current Topic: {state['current_topic']}"

    )

    if state["previous_topic"]:

        lines.append(

            f"Previous Topic: {state['previous_topic']}"

        )

    lines.append("")

    lines.append("Recent Conversation:")

    for item in state["history"][-5:]:

        lines.append(

            f"- [{item['topic']}] {item['message']}"

        )

    return "\n".join(lines)
# ===========================================
# Conversation Summary Compatibility Function
# ===========================================

def get_conversation_summary():

    """
    Compatibility wrapper used by the orchestrator.
    Returns the current conversation summary.
    """

    return get_summary()

# ===========================================
# Reset Conversation
# ===========================================

def reset_conversation():

    save_state(DEFAULT_STATE)


# ===========================================
# Test
# ===========================================

if __name__ == "__main__":

    print("=" * 50)

    print("TimiFX AI Conversation Engine Test")

    print("=" * 50)

    messages = [

        "I love Python",

        "Let's build an AI assistant",

        "Push this project to GitHub",

        "Create a Telegram bot",

        "How do I improve memory?"

    ]

    for message in messages:

        print()

        print("Message:")

        print(message)

        state = update_conversation(message)

        print()

        print("Detected Topic:")

        print(state["current_topic"])

    print()

    print("=" * 50)

    print("Conversation Summary")

    print("=" * 50)

    print()

    print(get_summary())