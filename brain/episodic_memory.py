"""
===========================================
TimiFX AI Episodic Memory
Phase 16
Author: Timilehin
===========================================

Stores important life events and milestones.
===========================================
"""

import json
import os
from datetime import datetime


EPISODIC_FILE = "database/episodic_memory.json"


def load_events():

    if not os.path.exists(EPISODIC_FILE):

        return []

    with open(
        EPISODIC_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_events(events):

    with open(
        EPISODIC_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            events,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_event(
    event,
    category="general",
    importance=5
):

    events = load_events()

    events.append(

        {

            "event": event,

            "category": category,

            "importance": importance,

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }

    )

    save_events(events)

    return events


def get_events():

    return sorted(

        load_events(),

        key=lambda x: x["importance"],

        reverse=True

    )


if __name__ == "__main__":

    add_event(

        "Completed Phase 16 of TimiFX AI",

        category="achievement",

        importance=10

    )

    add_event(

        "Started building episodic memory",

        category="development",

        importance=8

    )

    print(get_events())