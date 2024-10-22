#!/usr/bin/env python3
"""return list with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return list with a specific topic"""
    return mongo_collection.find({"topics": topic})
