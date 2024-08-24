#!/usr/bin/env python3
""" lists all documents in a collection """

from typing import List, Dict

def list_all(mongo_collection) -> List[Dict]:
    """ retrieves all documents from the specified collection """
    if collection:
        return list(mongo_collection.find())
    return []

