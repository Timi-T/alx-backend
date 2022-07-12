#!/usr/bin/env python3
"""
Basic caching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Function that implements a basic caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache memory"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache memory"""
        if key:
            return self.cache_data.get(key)
