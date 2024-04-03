#!/usr/bin/env python3
""" Module implementing an MRU (Most Recently Used) Cache. """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Implementation of MRU (Most Recently Used) Caching.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Constructor initializing the cache and a list to track usage order.
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
            if key in self.cache_data_list:
                self.cache_data_list.remove(key)
            self.cache_data_list.append(key)
            if len(self.cache_data_list) > BaseCaching.MAX_ITEMS:
                removed_key = self.cache_data_list.pop(-2)
                del self.cache_data[removed_key]
                print(f"DISCARD: {removed_key}")

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): Key of the item to retrieve.

        Returns:
            Item associated with the key, or None if key is not found.
        """
        if key in self.cache_data:
            self.cache_data_list.remove(key)
            self.cache_data_list.append(key)
            return self.cache_data[key]
        return None
