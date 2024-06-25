#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system that inherits from BaseCaching
        and uses an LFU algorithm for cache replacement
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.frequency = {}  # to keep track of the frequency of accesses
        self.order = []
        # to keep track of the order of accesses for tie-breaking

    def put(self, key, item):
        """ Add an item in the cache
            If the number of items in the cache exceeds the MAX_ITEMS, discard
            the least frequently used item (LFU)
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Find the least frequently used item
                    min_freq = min(self.frequency.values())
                    lfu_keys = [k for k, v in self.frequency.items()
                                if v == min_freq]
                    if len(lfu_keys) > 1:
                        lru_key = min(
                            lfu_keys,
                            key=lambda k: self.order.index(k)
                        )
                    else:
                        lru_key = lfu_keys[0]
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    self.order.remove(lru_key)
                    print(f"DISCARD: {lru_key}")
                self.frequency[key] = 0
            else:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            self.frequency[key] += 1

    def get(self, key):
        """ Get an item by key
            Return None if the key is None or if the key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        self.frequency[key] += 1
        return self.cache_data[key]
