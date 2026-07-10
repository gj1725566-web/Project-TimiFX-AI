"""
===========================================
TimiFX AI Tool Router Engine
Phase 24 - Multi Tool Routing Intelligence

Responsible for:

- Detecting required tool
- Routing requests
- Connecting Tool Manager
- Executing tools

Author: Timilehin
===========================================
"""


import sys
import os



PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)





from brain.tool_manager import (
    ToolManager,
    hello_tool
)


from tools.calculator_tool import (
    run as calculator_tool
)





# ===========================================
# Create Tool Manager
# ===========================================


manager = ToolManager()



# Register tools


manager.register_tool(

    "hello",

    hello_tool

)



manager.register_tool(

    "calculator",

    calculator_tool

)







# ===========================================
# Detect Tool
# ===========================================


def detect_tool(message):


    text = message.lower()



    if any(word in text for word in [

        "hello",
        "hi",
        "hey"

    ]):

        return "hello"




    if any(word in text for word in [

        "calculate",
        "calculator",
        "+",
        "-",
        "*",
        "/"

    ]):

        return "calculator"




    return None







# ===========================================
# Extract Calculator Expression
# ===========================================


def extract_expression(message):


    text = message.lower()


    for word in [

        "calculate",
        "calculator"

    ]:


        text = text.replace(
            word,
            ""
        )


    return text.strip()







# ===========================================
# Route Tool
# ===========================================


def route_tool(message):


    tool = detect_tool(
        message
    )



    if not tool:


        return {


            "success": False,


            "error":
            "No matching tool found.",


            "available_tools":
            manager.list_tools()

        }




    if tool == "hello":


        return manager.execute_tool(

            "hello",

            "Timilehin"

        )





    if tool == "calculator":


        expression = extract_expression(
            message
        )


        return manager.execute_tool(

            "calculator",

            expression

        )







# ===========================================
# Test
# ===========================================


if __name__ == "__main__":


    print("=" * 50)

    print(
        "TimiFX AI Tool Router Test"
    )

    print("=" * 50)



    tests = [

        "hello",

        "calculate 5+5",

        "calculator 100/4",

        "unknown request"

    ]



    for message in tests:


        print()

        print(
            "User:"
        )

        print(message)


        print()


        print(
            route_tool(message)
        )