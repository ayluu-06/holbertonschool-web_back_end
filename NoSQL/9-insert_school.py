#!/usr/bin/env python3
""" module documented
"""


def insert_school(mongo_collection, **kwargs):
    """ def documented
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
