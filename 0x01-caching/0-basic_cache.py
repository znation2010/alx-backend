#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        Store an item in the cache with the provided key.

        Args:
            key: The key to associate with the item in the cache.
            item: The item to be stored in the cache.

        Note:
            If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the item associated with the given key from the cache.

        Args:
            key: The key whose value needs to be retrieved.

        Returns:
            The item associated with the key if it exists in the cache.

        Note:
            If key is None or if the key doesn’t exist in the cache.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
