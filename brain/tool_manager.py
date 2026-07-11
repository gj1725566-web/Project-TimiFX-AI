"""
===========================================
TimiFX AI Tool Manager
Author: Timilehin
Version: 1.0

The Tool Manager is responsible for:

- Registering AI tools
- Finding available tools
- Checking if a tool exists
- Executing tools
- Listing installed tools

Future tools include:

- Python Executor
- File Reader
- Web Search
- Vision
- Calculator
- APIs
===========================================
"""


class ToolManager:

    def __init__(self):

        self.tools = {}

    # ======================================
    # Register Tool
    # ======================================

    def register_tool(
        self,
        name,
        function
    ):

        self.tools[name] = function

    # ======================================
    # Tool Exists
    # ======================================

    def has_tool(
        self,
        name
    ):

        return name in self.tools

    # ======================================
    # Execute Tool
    # ======================================

    def execute_tool(
        self,
        name,
        *args,
        **kwargs
    ):

        if not self.has_tool(name):

            return {

                "success": False,

                "error": f"Tool '{name}' is not registered."

            }

        try:

            result = self.tools[name](
                *args,
                **kwargs
            )

            return {

                "success": True,

                "result": result

            }

        except Exception as error:

            return {

                "success": False,

                "error": str(error)

            }

    # ======================================
    # List Tools
    # ======================================

    def list_tools(self):

        return sorted(self.tools.keys())


# ==========================================
# Demo Tool
# ==========================================

def hello_tool(name):

    return f"Hello {name}! Welcome to TimiFX AI."


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print("TimiFX AI Tool Manager Test")
    print("=" * 50)

    manager = ToolManager()

    manager.register_tool(

        "hello",

        hello_tool

    )

    print()

    print("Installed Tools:")

    print(

        manager.list_tools()

    )

    print()

    print("Executing Tool:")

    print(

        manager.execute_tool(

            "hello",

            "Timilehin"

        )

    )

    print()

    print("Executing Missing Tool:")

    print(

        manager.execute_tool(

            "python"

        )

    )