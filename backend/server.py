"""
===========================================
TimiFX AI Backend Server
Phase 12 - Full Brain Pipeline Integration
Author: Timilehin
===========================================
"""


import sys
import os


# Add project root directory to Python path

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )



from flask import Flask, request, jsonify

from flask_cors import CORS

from datetime import datetime



from brain.pipeline import run_pipeline


from database.memory import (
    save_conversation,
    get_conversation_history
)



app = Flask(__name__)


CORS(app)





@app.route("/", methods=["GET"])
def home():


    return jsonify({

        "project": "TimiFX AI",

        "status": "online",

        "brain": "Pipeline Active",

        "systems": [

            "Reasoning Engine",

            "Planning Engine",

            "Knowledge Memory",

            "Conversation Memory",

            "AI Engine"

        ],

        "version": "Phase 12",

        "time": str(
            datetime.now()
        )

    })







@app.route("/chat", methods=["POST"])
def chat():


    data = request.get_json()



    if not data:


        return jsonify({

            "error":
            "No JSON received."

        }), 400





    user_message = data.get(

        "message",

        ""

    ).strip()





    if not user_message:


        return jsonify({

            "error":
            "Message cannot be empty."

        }), 400






    try:


        # Send message through full TimiFX brain pipeline

        pipeline_result = run_pipeline(

            user_message

        )



        ai_reply = pipeline_result[

            "response"

        ]



    except Exception as error:


        return jsonify({

            "error":
            str(error)

        }), 500






    # Save conversation memory


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







    return jsonify({

        "user_message":

            user_message,



        "ai_response":

            ai_reply,



        "reasoning":

            pipeline_result.get(

                "reasoning",

                {}

            ),



        "plan":

            pipeline_result.get(

                "plan",

                {}

            ),



        "knowledge_used":

            pipeline_result.get(

                "knowledge",

                {}

            ),



        "memory_used":

            pipeline_result.get(

                "memory_used",

                False

            ),



        "memory_count":

            len(

                get_conversation_history(

                    "Timilehin"

                )

            ),



        "time":

            str(

                datetime.now()

            )

    })







if __name__ == "__main__":


    print(
        "🚀 TimiFX AI Backend Running..."
    )


    print(
        "🧠 AI Engine Loaded"
    )


    print(
        "💾 Memory System Loaded"
    )


    print(
        "🤔 Reasoning Engine Loaded"
    )


    print(
        "📋 Planning Engine Loaded"
    )


    print(
        "🔗 Full Brain Pipeline Connected"
    )



    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )