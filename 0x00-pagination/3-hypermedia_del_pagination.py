#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


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
            truncated_dataset = dataset[:1000]  # Use a subset for indexing
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Get items for the given starting index with hypermedia metadata
        Args:
            index (int): starting index of the dataset page (default: None)
            page_size (int): number of items per page (default: 10)
        Returns:
            (Dict[str, Any]): a dictionary with hypermedia pagination info
        """
        indexed_dataset = self.indexed_dataset()
        dataset_length = len(indexed_dataset)
        if index is not None:
            assert 0 <= index < dataset_length, "Index out of range"

        if index is None or index not in indexed_dataset:
            index = 0
            while index < dataset_length and index not in indexed_dataset:
                index += 1
            if index >= dataset_length:
                return {
                    'index': 0,
                    'next_index': None,
                    'page_size': 0,
                    'data': []
                }

        next_index = index + page_size
        data = [
            indexed_dataset[i] for i in range(
                index, min(index + page_size, dataset_length)
            )
        ]

        return {
            'index': index,
            'next_index': next_index if next_index < dataset_length else None,
            'page_size': len(data),
            'data': data
        }
