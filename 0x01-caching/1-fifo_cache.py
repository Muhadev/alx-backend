#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that inherits from BaseCaching
        and uses a FIFO algorithm for cache replacement
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.order = []  # to keep track of the order of insertion

    def put(self, key, item):
        """ Add an item in the cache
            If the number of items in the cache exceeds the MAX_ITEMS, discard
            the first added item (FIFO)
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print(f"DISCARD: {first_key}")
            elif key in self.order:
                self.order.remove(key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
            Return None if the key is None or if the key doesn't exist
        """
        return self.cache_data.get(key, None)
