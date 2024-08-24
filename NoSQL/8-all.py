#!/usr/bin/env python3
""" Lists all documents in a collection """

from typing import List, Dict

def list_all(mongo_collection) -> List[Dict]:
    """ Retrieves all documents from the specified collection.

    Args:
        mongo_collection: The pymongo collection object to query.

    Returns:
        A list of documents in the collection. Returns an empty list if no documents are found.
    """
    if mongo_collection:
        return list(mongo_collection.find())
    return []

