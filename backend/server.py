import sys
import os

# ===========================================
# Add Project Root
# ===========================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ===========================================
# Imports
# ===========================================

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

from backend.ai_engine import generate_response

from brain.reasoning import analyze_intent

from database.memory import (
    save_conversation,
    get_conversation_history
)


# ===========================================
# Flask
# ===========================================

app = Flask(__name__)

CORS(app)


# ===========================================
# Home
# ===========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "project": "TimiFX AI",

        "version": "Phase 11",

        "status": "online",

        "ai_engine": "Groq",

        "reasoning": "Enabled",

        "memory": "Conversation Memory Active",

        "time": str(datetime.now())

    })


# ===========================================
# Chat
# ===========================================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:

        return jsonify({

            "error": "No JSON received."

        }), 400


    user_message = data.get(
        "message",
        ""
    ).strip()


    if user_message == "":

        return jsonify({

            "error": "Message cannot be empty."

        }), 400


    # =======================================
    # Analyze User Intent
    # =======================================

    reasoning = analyze_intent(
        user_message
    )


    # =======================================
    # Load Memory
    # =======================================

    conversation = []

    if reasoning["use_memory"]:

        conversation = get_conversation_history(
            "Timilehin"
        )


    # Add newest message

    conversation.append({

        "role": "user",

        "content": user_message

    })


    # =======================================
    # Generate AI Response
    # =======================================

    try:

        ai_reply = generate_response(
            conversation
        )

    except Exception as error:

        return jsonify({

            "error": str(error)

        }), 500


    # =======================================
    # Save Memory
    # =======================================

    save_conversation(

        "Timilehin",

        "user",

        user_message

    )

    save_conversation(

        "Timilehin",

        "assistant",

        ai_reply

    )


    # =======================================
    # Response
    # =======================================

    return jsonify({

        "user_message": user_message,

        "intent": reasoning["intent"],

        "memory_used": reasoning["use_memory"],

        "knowledge_used": reasoning["use_knowledge"],

        "ai_response": ai_reply,

        "memory_count": len(

            get_conversation_history(

                "Timilehin"

            )

        ),

        "time": str(datetime.now())

    })


# ===========================================
# Main
# ===========================================

if __name__ == "__main__":

    print("🚀 TimiFX AI Backend Running...")

    print("🧠 AI Engine Loaded")

    print("💾 Memory System Loaded")

    print("🤔 Reasoning Engine Loaded")

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )