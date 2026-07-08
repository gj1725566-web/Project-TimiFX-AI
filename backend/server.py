import sys
import os


# Add project root directory to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq


from database.memory import (
    save_memory,
    get_memory
)



# Load environment variables
load_dotenv()


# Get Groq API Key
GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)


# Check API key
if not GROQ_API_KEY:

    raise ValueError(
        "GROQ_API_KEY missing. Check your .env file."
    )



# Create Groq client
client = Groq(
    api_key=GROQ_API_KEY
)



app = Flask(__name__)

CORS(app)



# ==========================
# HOME ROUTE
# ==========================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "project":
        "TimiFX AI",

        "status":
        "online",

        "message":
        "Welcome to TimiFX AI Core Engine",

        "ai_engine":
        "Groq",

        "memory":
        "Active",

        "time":
        str(datetime.now())

    })





# ==========================
# CHAT ROUTE
# ==========================

@app.route("/chat", methods=["POST"])
def chat():


    data = request.json


    user_message = data.get(
        "message",
        ""
    )


    if user_message == "":

        return jsonify({

            "error":
            "Message cannot be empty"

        })



    # Save user memory

    save_memory(

        "Timilehin",

        user_message

    )



    try:


        memory = get_memory(
            "Timilehin"
        )



        response = client.chat.completions.create(


            model=
            "llama-3.3-70b-versatile",


            messages=[


                {

                    "role":
                    "system",


                    "content":
                    """
You are TimiFX AI.

Your identity:

- Your name is TimiFX AI.
- You are Timilehin's personal AI assistant.
- You help with technology, programming,
  business ideas, automation, AI projects,
  learning, and productivity.

Personality:

- Friendly
- Professional
- Intelligent
- Encouraging
- Clear and detailed

Important:

Remember that Timilehin is your founder
and creator.

The current project is:
Project-TimiFX-AI.

You should always behave like a
professional AI assistant built for
this project.

Previous memory:

"""
+
str(memory)

                },


                {

                    "role":
                    "user",


                    "content":
                    user_message

                }

            ]

        )



        ai_reply = (

            response
            .choices[0]
            .message
            .content

        )




    except Exception as error:


        ai_reply = (

            "TimiFX AI encountered an error: "
            + str(error)

        )





    return jsonify({


        "project":

        "TimiFX AI",



        "user_message":

        user_message,



        "ai_response":

        ai_reply,



        "memory":

        get_memory(
            "Timilehin"
        ),



        "time":

        str(datetime.now())

    })






# ==========================
# START SERVER
# ==========================


if __name__ == "__main__":


    print(
        "🚀 TimiFX AI Backend Running..."
    )


    print(
        "🧠 Groq Intelligence Online"
    )


    print(
        "💾 Memory System Connected"
    )



    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )