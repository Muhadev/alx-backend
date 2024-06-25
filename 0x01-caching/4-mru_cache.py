#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system that inherits from BaseCaching
        and uses an MRU algorithm for cache replacement
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.order = []  # to keep track of the order of access

    def put(self, key, item):
        """ Add an item in the cache
            If the number of items in the cache
            exceeds the MAX_ITEMS, discard
            the most recently used item (MRU)
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    mru_key = self.order.pop()
                    del self.cache_data[mru_key]
                    print(f"DISCARD: {mru_key}")
            elif key in self.order:
                self.order.remove(key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
            Return None if the key is None or if the key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
