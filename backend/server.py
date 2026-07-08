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
    save_conversation,
    get_conversation_history
)



# Load environment variables
load_dotenv()



GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)



client = Groq(
    api_key=GROQ_API_KEY
)



app = Flask(__name__)

CORS(app)




@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "project": "TimiFX AI",

        "status": "online",

        "ai_engine": "Groq",

        "memory": "Conversation Memory Active",

        "time": str(datetime.now())

    })





@app.route("/chat", methods=["POST"])
def chat():

    data = request.json


    user_message = data.get(
        "message",
        ""
    )



    # Load previous conversation
    history = get_conversation_history(
        "Timilehin"
    )



    messages = [

        {
            "role": "system",

            "content":
            """
You are TimiFX AI.

You are an intelligent personal AI assistant.

Founder:
Timilehin

Project:
Project-TimiFX-AI

Personality:
Helpful,
professional,
creative,
friendly.

Remember previous conversations
when answering.
"""
        }

    ]



    # Add previous memory
    messages.extend(history)



    # Add current user message
    messages.append(

        {

            "role": "user",

            "content": user_message

        }

    )




    try:


        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=messages

        )



        ai_reply = (

            response
            .choices[0]
            .message
            .content

        )



    except Exception as error:


        ai_reply = (

            "TimiFX AI Error: "

            + str(error)

        )





    # Save user message
    save_conversation(

        "Timilehin",

        "user",

        user_message

    )



    # Save AI response
    save_conversation(

        "Timilehin",

        "assistant",

        ai_reply

    )





    return jsonify({

        "user_message":

        user_message,


        "ai_response":

        ai_reply,


        "memory":

        get_conversation_history(

            "Timilehin"

        ),


        "time":

        str(datetime.now())

    })






if __name__ == "__main__":


    print(
        "🚀 TimiFX AI Backend Running..."
    )


    print(
        "🧠 Groq + Memory System Connected"
    )


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )