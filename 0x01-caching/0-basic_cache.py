#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that inherits from BaseCaching
        This caching system has no limit on the number of items
    """

    def put(self, key, item):
        """ Add an item in the cache
            If key or item is None, this method should not do anything
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
            Return None if key is None or if the key doesn't
            exist in cache_data
        """
        return self.cache_data.get(key, None)
