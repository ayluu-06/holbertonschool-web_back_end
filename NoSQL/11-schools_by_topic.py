#!/usr/bin/env python3
""" module documented
"""


def schools_by_topic(mongo_collection, topic):
    """ def documented
    """
    return mongo_collection.find({"topics": topic})
