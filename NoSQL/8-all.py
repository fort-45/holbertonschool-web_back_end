#!/usr/bin/env python3
"""doc doc doc"""
def list_all(mongo_collection):
    """list all documents in a collection"""
    return list(mongo_collection.find())
