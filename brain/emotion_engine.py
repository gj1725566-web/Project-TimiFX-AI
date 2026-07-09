"""
===========================================
TimiFX AI Emotion Engine
Phase 18 - Emotional Intelligence Layer

Author: Timilehin
===========================================
"""


EMOTION_PATTERNS = {

    "happy": [

        "happy",
        "excited",
        "great",
        "amazing",
        "awesome",
        "love",
        "enjoy",
        "proud",
        "fantastic",
        "wonderful"

    ],


    "sad": [

        "sad",
        "unhappy",
        "depressed",
        "lonely",
        "hurt",
        "cry",
        "disappointed"

    ],


    "confused": [

        "confused",
        "don't understand",
        "unclear",
        "lost",
        "help me understand"

    ],


    "frustrated": [

        "frustrated",
        "frustrating",
        "annoyed",
        "angry",
        "stress",
        "stressed",
        "overwhelmed",
        "tired",
        "difficult",
        "hard"

    ]

}





def detect_emotion(message):

    """
    Analyze user emotional state.
    """

    text = message.lower()


    detected = []


    for emotion, words in EMOTION_PATTERNS.items():

        for word in words:

            if word in text:

                detected.append(
                    emotion
                )

                break



    if not detected:

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







def emotion_response_style(emotion):


    styles = {


        "happy":
        "Respond positively and celebrate the user's excitement.",


        "sad":
        "Respond with empathy, patience, and encouragement.",


        "confused":
        "Explain clearly and step-by-step.",


        "frustrated":
        "Respond calmly, acknowledge difficulty, and provide supportive guidance.",


        "neutral":
        "Respond normally."

    }


    return styles.get(

        emotion,

        "Respond normally."

    )








if __name__ == "__main__":


    print("="*50)

    print(
        "TimiFX AI Emotion Engine Test"
    )

    print("="*50)



    tests = [

        "I am so excited about building AI tools",

        "I feel sad today",

        "I am confused about Python",

        "This project is frustrating",

        "Hello how are you"

    ]



    for message in tests:


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
            emotion_response_style(
                result["emotion"]
            )
        )