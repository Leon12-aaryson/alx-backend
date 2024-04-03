#!/usr/bin/env python3
""" Module containing the FIFOCache class inheriting from BaseCaching. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Subclass of BaseCaching implementing a FIFO cache replacement policy.
    """
    def __init__(self):
        """ Initializes a FIFOCache instance. """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        Adds an item into the cache.

        Args:
            key (str): Key of the item.
            item: Item to add.
        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_data_list.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): Key of the item to retrieve.

        Returns:
            Item associated with the key, or None if not found.
        """
        return self.cache_data.get(key)
