#!/usr/bin/python3
"""
simple function to ensure user does not miss items
from a dataset when changed
"""


from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        dataset = self.dataset()
        data_length = len(dataset)

        if index is None:
            index = 0
        else:
            assert 0 <= index < data_length, "Index out of range"

        next_index = min(index + page_size, data_length)
        data = dataset[index:next_index]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
