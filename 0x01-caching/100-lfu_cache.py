#!/usr/bin/env python3

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Implementation of LFU (Least Frequently Used) Caching.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Constructor initializing the cache, a dictionary to track frequency,
        and a variable to keep track of minimum frequency.
        """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key: Key of the item.
            item: Item to add.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq_keys = self.frequency.get(self.min_frequency, [])
            discard_key = min_freq_keys.pop(0)
            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            print("DISCARD:", discard_key)

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.min_frequency = 1

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key: Key of the item to retrieve.

        Returns:
            Item associated with the key, or None if key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        return self.cache_data[key]
