#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection with specified attributes"""

def insert_document(collection, **attributes):
    """
    Inserts a new document into a specified MongoDB collection.

    Args:
        collection: The MongoDB collection where the document will be inserted.
        **attributes: Key-value pairs representing the document's fields.

    Returns:
        The unique identifier (_id) of the newly inserted document.
    """
    document = {}
    for key, value in attributes.items():
        document[key] = value

    result = collection.insert_one(document)
    return result.inserted_id

