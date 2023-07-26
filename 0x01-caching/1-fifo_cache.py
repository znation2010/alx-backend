#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """
        Initialize the FIFO cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Store an item in the FIFO cache with the provided key.

        Args:
            key: The key to associate with the item in the cache.
            item: The item to be stored in the cache.

        Note:
            If key or item is None, this method does nothing.
            If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS,
            the method will discard the first item put in the cache using FIFO algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Get the first key in the cache (FIFO)
                first_key = next(iter(self.cache_data))
                # Discard the item associated with the first key
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}\n")

            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the item associated with the given key from the FIFO cache.

        Args:
            key: The key whose value needs to be retrieved.

        Returns:
            The item associated with the key if it exists in the cache, None otherwise.

        Note:
            If key is None or if the key doesn’t exist in the cache, return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
