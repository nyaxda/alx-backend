#!/usr/bin/python3
""" BaseCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system and inherits from BaseCaching
    """
    def put(self, key, item):
        """ Method that add key and value to the dict
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Method that gets value of key stored in the dict"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
