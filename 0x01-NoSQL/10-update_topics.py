#!/usr/bin/env python3
"""update document"""


def update_topics(mongo_collection, name, topics):
    """update school document"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
