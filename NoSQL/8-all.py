#!/usr/bin/env python3
"""  lists all documents in a collection """


def list_all(mongo_collection):
    """ Method that will lists all docs """
    return list(mongo_collection.find())
