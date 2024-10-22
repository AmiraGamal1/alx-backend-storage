#!/usr/bin/env python3
"""Insert document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert new document in a collection"""
    ins = mongo_collection.insert_one(kwargs)

    return ins.inserted_id
