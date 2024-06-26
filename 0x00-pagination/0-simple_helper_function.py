#!/usr/bin/env python3
""" Simple helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a size 2 tuple """
    start = 0
    end = 0
    for p in range(page):
        start = end
        end = start + page_size
    return (start, end)
