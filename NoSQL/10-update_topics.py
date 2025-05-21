#!/usr/bin/env python3
""" module documented
"""


def update_topics(mongo_collection, name, topics):
    """ def documented
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
