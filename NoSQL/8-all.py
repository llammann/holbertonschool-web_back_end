#!/usr/bin/env python3
""" lists all documents in a collection """

from typing import List, Dict

def list_all(collection) -> List[Dict]:
    """ retrieves all documents from the specified collection """
    if collection:
        return list(collection.find())
    return []

