"""
===========================================
TimiFX AI Conversation Engine
Phase 25 - Conversation Intelligence Upgrade

Responsibilities:

- Topic Detection
- Conversation State Management
- Duplicate Protection
- Conversation Summary
- Memory Cleanup
- Session Control

Author: Timilehin
===========================================
"""

import json
import os
import hashlib
from datetime import datetime


# ===========================================
# Database Location
# ===========================================

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


# ===========================================
# Settings
# ===========================================

MAX_HISTORY = 25


# ===========================================
# Default Conversation State
# ===========================================

DEFAULT_STATE = {

    "current_topic": "General",

    "previous_topic": "",

    "session_started":

        str(datetime.now()),

    "history": []

}



# ===========================================
# Message Hash
# ===========================================

def create_message_hash(message):

    return hashlib.md5(

        message.strip()
        .lower()
        .encode()

    ).hexdigest()



# ===========================================
# Load State
# ===========================================

def load_state():

    if not os.path.exists(DATABASE):

        save_state(DEFAULT_STATE)

        return DEFAULT_STATE.copy()


    try:

        with open(
            DATABASE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except:

        save_state(DEFAULT_STATE)

        return DEFAULT_STATE.copy()



# ===========================================
# Save State
# ===========================================

def save_state(state):

    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            state,

            file,

            indent=4,

            ensure_ascii=False

        )



# ===========================================
# Topic Detection
# ===========================================

def detect_topic(message):

    text = message.lower()


    topics = {


        "Python":

        [

            "python",
            "coding",
            "programming",
            "script"

        ],



        "Artificial Intelligence":

        [

            "ai",
            "assistant",
            "chatbot",
            "machine learning",
            "llm"

        ],



        "Memory System":

        [

            "memory",
            "profile",
            "remember"

        ],



        "Git/GitHub":

        [

            "git",
            "github",
            "commit",
            "push",
            "branch"

        ],



        "Telegram Bot":

        [

            "telegram",
            "bot",
            "botfather"

        ],



        "Web Development":

        [

            "website",
            "flask",
            "fastapi",
            "api"

        ],



        "Mathematics":

        [

            "calculate",
            "math",
            "+",
            "-",
            "*",
            "/"

        ]

    }



    for topic, keywords in topics.items():

        for keyword in keywords:

            if keyword in text:

                return topic



    return "General"



# ===========================================
# Update Conversation
# ===========================================

def update_conversation(message):


    state = load_state()


    topic = detect_topic(message)


    message_hash = create_message_hash(
        message
    )



    # ---------------------------------------
    # Prevent duplicate messages
    # ---------------------------------------

    for item in state["history"]:

        if item.get("hash") == message_hash:

            return state



    # ---------------------------------------
    # Update topics
    # ---------------------------------------

    if topic != state["current_topic"]:

        state["previous_topic"] = (
            state["current_topic"]
        )


        state["current_topic"] = topic



    # ---------------------------------------
    # Add new conversation
    # ---------------------------------------

    state["history"].append(

        {

            "message": message,

            "topic": topic,

            "hash": message_hash,

            "time": str(datetime.now())

        }

    )



    # ---------------------------------------
    # Memory cleanup
    # ---------------------------------------

    if len(state["history"]) > MAX_HISTORY:

        state["history"] = (

            state["history"][-MAX_HISTORY:]

        )



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

def get_conversation_summary():

    state = load_state()


    summary = []


    summary.append(

        f"Current Topic: {state['current_topic']}"

    )


    if state["previous_topic"]:

        summary.append(

            f"Previous Topic: {state['previous_topic']}"

        )


    summary.append("")


    summary.append(
        "Recent Conversation:"
    )



    for item in state["history"][-5:]:


        summary.append(

            f"- [{item['topic']}] {item['message']}"

        )


    return "\n".join(summary)



# ===========================================
# Alias
# ===========================================

def get_summary():

    return get_conversation_summary()



# ===========================================
# Reset Conversation
# ===========================================

def reset_conversation():

    save_state(
        DEFAULT_STATE
    )



# ===========================================
# Test
# ===========================================

if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Conversation Engine Test"
    )

    print("=" * 50)



    reset_conversation()



    tests = [

        "I love Python",

        "Let's build an AI assistant",

        "Push this project to GitHub",

        "Create a Telegram bot",

        "How do I improve memory?",

        "How do I improve memory?"

    ]



    for message in tests:


        print()

        print(
            "Message:"
        )

        print(message)


        result = update_conversation(
            message
        )


        print()

        print(
            "Current Topic:"
        )

        print(
            result["current_topic"]
        )



    print()

    print("=" * 50)

    print(
        "Summary"
    )

    print("=" * 50)


    print(
        get_conversation_summary()
    )