/*
===========================================
TimiFX AI Website Chat Engine v2.0
Author: Timilehin
===========================================
*/


const chatBox = document.getElementById("chatBox");
const userMessage = document.getElementById("userMessage");
const sendBtn = document.getElementById("sendBtn");



// Add message to chat window

function addMessage(message, sender) {


    const messageDiv = document.createElement("div");


    messageDiv.classList.add(
        "message",
        sender
    );


    messageDiv.innerText = message;


    chatBox.appendChild(
        messageDiv
    );


    chatBox.scrollTop =
        chatBox.scrollHeight;

}





// Send message to TimiFX AI

async function sendMessage() {


    const message =
        userMessage.value.trim();



    if(message === "") {

        return;

    }



    addMessage(
        message,
        "user"
    );



    userMessage.value = "";



    addMessage(
        "TimiFX AI is thinking...",
        "ai"
    );



    try {


        const response =
        await fetch(
            "http://127.0.0.1:5000/chat",
            {


                method:
                "POST",


                headers:
                {

                    "Content-Type":
                    "application/json"

                },


                body:
                JSON.stringify({

                    message:
                    message

                })

            }

        );



        const data =
        await response.json();



        // Remove thinking message

        chatBox.lastChild.remove();



        addMessage(

            data.ai_response,

            "ai"

        );



    }



    catch(error) {



        chatBox.lastChild.remove();



        addMessage(

            "Connection error. Make sure TimiFX AI backend is running.",

            "ai"

        );


        console.error(
            error
        );


    }


}




// Button click

sendBtn.addEventListener(
    "click",
    sendMessage
);




// Enter key support

userMessage.addEventListener(

    "keypress",

    function(event){


        if(event.key === "Enter") {


            sendMessage();


        }


    }

);