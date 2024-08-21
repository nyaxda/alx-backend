#!/usr/bin/python3
""" FIFO Caching
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """FIFO caching class inheriting from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """method for adding an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data and len(
             self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.popleft()
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

        if key not in self.cache_data:
            self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """method for accessing values of a key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
