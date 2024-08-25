#!/usr/bin/env python3
""" Write a Python function that lists all documents in a collection """

from pymongo.collection import Collection

def list_all(mongo_collection: Collection):
    """ Lists all documents in a collection.
    
    Args:
        mongo_collection (Collection): The pymongo collection object.
        
    Returns:
        List[dict]: A list of all documents in the collection.
    """
    return list(mongo_collection.find()) if mongo_collection else []

