#!/usr/bin/python3
""" MRU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU caching class inheriting from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """method for adding an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(False)
            print("DISCARD: {}".format(discarded_key))
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

    def get(self, key):
        """method for accessing values of a key"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
