#!/usr/bin/env python3
"""
Module contains class BasicCache that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class implementing a basic caching system.
    Inherits from BaseCaching.
    """
    def __init__(self):
        """
        Initializes a BasicCache instance.
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key (str): Key of the item.
            item (str): Item to be added.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the key from the cache.

        Args:
            key (str): Key to retrieve the value.

        Returns:
            Value associated with the key, or None if key is not in the cache.
        """
        return self.cache_data.get(key)
