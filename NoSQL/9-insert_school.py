#!/usr/bin/env python3
""" 9. Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """ inserts new doc in collection based on kwargs """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
