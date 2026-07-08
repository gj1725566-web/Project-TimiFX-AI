import sys
import os

# ==========================================
# Add project root to Python path
# ==========================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# ==========================================
# Imports
# ==========================================

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

from database.memory import (
    save_memory,
    get_memory
)

# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)

CORS(app)

# ==========================================
# Home Route
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "project": "TimiFX AI",

        "status": "online",

        "message": "Welcome to TimiFX AI Core Engine",

        "time": str(datetime.now())

    })

# ==========================================
# Chat Route
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "").strip()

    if user_message == "":

        return jsonify({

            "response": "Please type a message."

        })

    # Save message into memory
    save_memory(
        "Timilehin",
        user_message
    )

    # Read memory
    memory = get_memory("Timilehin")

    # AI reply
    ai_reply = (
        f"You said: '{user_message}'. "
        "Your message has been saved into memory."
    )

    return jsonify({

        "response": ai_reply,

        "memory": memory,

        "time": str(datetime.now())

    })

# ==========================================
# Run Server
# ==========================================

if __name__ == "__main__":

    print("🚀 TimiFX AI Backend Running...")

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )