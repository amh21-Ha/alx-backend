#!/usr/bin/env python3
""" FIFO Caching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements a
    FIFO caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm """
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Update existing key's value, maintain the order
            self.cache_data[key] = item
        else:
            # Add new key-value pair
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first added item in the FIFO order
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
