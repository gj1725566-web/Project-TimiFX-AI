/* ===========================================
   TimiFX AI Website v2.0
   Frontend Backend Connection
   Author: Timilehin
=========================================== */


const sendButton = document.getElementById("sendBtn");

const userMessage = document.getElementById("userMessage");

const chatBox = document.getElementById("chatBox");





sendButton.addEventListener("click", async function(){


    const message = userMessage.value.trim();



    if(message === ""){

        return;

    }




    // Show user's message

    const userText = document.createElement("p");

    userText.innerHTML = "You: " + message;

    chatBox.appendChild(userText);





    userMessage.value = "";





    try {


        const response = await fetch(
            "http://127.0.0.1:5000/chat",
            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },


                body:JSON.stringify({

                    message:message

                })


            }
        );





        const data = await response.json();





        const aiText = document.createElement("p");


        aiText.innerHTML = 
        "🤖 TimiFX AI: " + data.response;




        chatBox.appendChild(aiText);




    }



    catch(error){


        const errorText = document.createElement("p");


        errorText.innerHTML =
        "❌ Connection error. Backend is not responding.";


        chatBox.appendChild(errorText);



        console.log(error);


    }



});