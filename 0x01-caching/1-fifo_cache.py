#!/usr/bin/env python3
"""
Basic caching module
"""

import queue
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Function that implements a basic caching system"""

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache memory"""
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.cache_data:
            key_pop = self.queue.pop(0)
            self.cache_data.pop(key_pop)
            print("DISCARD: {}".format(key_pop))
        if key and item:
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item from cache memory"""
        if key:
            return self.cache_data.get(key)
