#!/usr/bin/env python3
""" Module implementing LIFO Caching. """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Implementation of LIFO (Last In, First Out) caching strategy.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Constructor initializing the cache and a list to
        track order of insertion.
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key (str): Key of the item.
            item: Item to add.
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_data_list.pop(-2)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): Key of the item to retrieve.

        Returns:
            Item associated with the key, or None if key is not found.
        """
        return self.cache_data.get(key)
