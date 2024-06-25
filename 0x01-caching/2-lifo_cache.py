#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that inherits from BaseCaching
        and uses a LIFO algorithm for cache replacement
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
            If the number of items in the cache exceeds the MAX_ITEMS, discard
            the last added item (LIFO)
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    last_key = list(self.cache_data.keys())[-1]
                    del self.cache_data[last_key]
                    print(f"DISCARD: {last_key}")
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
            Return None if the key is None or if the key doesn't exist
        """
        return self.cache_data.get(key, None)
