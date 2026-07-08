"""
===========================================
Memory Manager
===========================================
"""

from database.memory import get_conversation_history


def load_recent_memory(name, limit=10):
    """
    Return only the most recent conversation messages.
    """

    conversation = get_conversation_history(name)

    return conversation[-limit:]