#!/usr/bin/env python3
"""doc doc doc"""
def insert_school(mongo_collection, **kwargs):
    """document insert 
    kwargs"""
    result = mongo_collection.insert_one(kwargs)
    """inserts a single doc"""
    return result.inserted_id
    """to return the id"""
