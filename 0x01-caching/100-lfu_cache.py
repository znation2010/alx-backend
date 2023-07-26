#!/usr/bin/python3
"""Least Frequently Used caching module.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class represents a Least Frequently Used (LFU)t.
    Methods:
        put(key, item): Add a key/value pair to the cache.
        get(key): Get the value associated with the given key from the cache.
    """

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.key_uses = {}  # Dictionary to store the usage count of each key.

    def put(self, key, item):
        """Add an item to the LFU cache."""
        if key is None or item is None:
            return
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.cache_data:
            least_used_key = min(self.key_uses, key=self.key_uses.get)
            del self.cache_data[least_used_key]
            del self.key_uses[least_used_key]
            print("DISCARD: {}".format(least_used_key))

        # Update the usage count of the key and store the item in the cache.
        if key in self.cache_data:
            self.key_uses[key] += 1
        else:
            self.key_uses[key] = 1

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key from the LFU cache."""
        if key is None or key not in self.cache_data:
            return None

        # Increment the usage count of the key and return the associated item.
        self.key_uses[key] += 1
        return self.cache_data.get(key)
