"""
===========================================
TimiFX AI Emotion Intelligence Engine

Author: Timilehin

Purpose:
Detect user emotions and provide response guidance.
===========================================
"""


# ===========================================
# Emotion keyword database
# ===========================================


EMOTION_KEYWORDS = {


    "happy": [

        "happy",
        "excited",
        "great",
        "amazing",
        "awesome",
        "love",
        "wonderful",
        "proud"

    ],



    "sad": [

        "sad",
        "unhappy",
        "depressed",
        "lonely",
        "hurt",
        "cry"

    ],



    "confused": [

        "confused",
        "don't understand",
        "unclear",
        "lost",
        "stuck"

    ],



   "frustrated": [

    "frustrated",
    "frustrating",
    "frustration",
    "annoyed",
    "annoying",
    "difficult",
    "problem",
    "issue",
    "not working",
    "stressful",
    "stuck"

],



    "angry": [

        "angry",
        "mad",
        "hate",
        "furious"

    ]

}




# ===========================================
# Detect emotion
# ===========================================


def detect_emotion(message):


    text = message.lower()



    detected = []



    for emotion, keywords in EMOTION_KEYWORDS.items():


        for keyword in keywords:


            if keyword in text:

                detected.append(
                    emotion
                )

                break





    if len(detected) == 0:


        return {

            "emotion": "neutral",

            "confidence": "low",

            "all_detected": []

        }





    primary = detected[0]



    return {


        "emotion": primary,


        "confidence": "high",


        "all_detected": detected


    }





# ===========================================
# Convert emotion into AI behavior
# ===========================================


def emotion_instruction(emotion_data):


    emotion = emotion_data.get(

        "emotion",

        "neutral"

    )



    instructions = {


        "happy":

        "Respond positively, celebrate the user's excitement, and maintain an encouraging tone.",



        "sad":

        "Respond with empathy, patience, and encouragement.",



        "confused":

        "Explain clearly and step-by-step.",



        "frustrated":

        "Respond calmly, acknowledge difficulty, and provide supportive guidance.",



        "angry":

        "Remain calm, respectful, and avoid escalating the situation.",



        "neutral":

        "Respond normally."

    }



    return instructions.get(

        emotion,

        instructions["neutral"]

    )






# ===========================================
# Test
# ===========================================


if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Emotion Engine Test"
    )

    print("=" * 50)



    test_messages = [


        "I am so excited about building AI tools",


        "I feel sad today",


        "I am confused about Python",


        "This project is frustrating",


        "Hello how are you"

    ]




    for message in test_messages:


        result = detect_emotion(
            message
        )


        print()

        print(
            "Message:",
            message
        )


        print(
            result
        )


        print(
            emotion_instruction(result)
        )