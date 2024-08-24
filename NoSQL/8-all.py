#!/usr/bin/env python3
""" lists all documents in a collection """

from pymongo import MongoClient
fetch_all_documents = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    all_schools = fetch_all_documents(school_collection)
    for school in all_schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))

