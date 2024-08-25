#!/usr/bin/env python3
""" 11. Where can I learn Python? """


def update_topics(mongo_collection, name, topics):
    """ returns the list of school having a specific topic """
    name_field = {"name": name}
    value_field = {"$set": {"topics": topics}}
    mongo_collection.update_many(name_field, value_field)
