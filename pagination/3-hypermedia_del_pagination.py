#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads the dataset from the CSV file, caching it after the first load."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Returns the dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves a page from the dataset with deletion-resilience.

        Args:
        - index (int): The starting index for the page.
        - page_size (int): The number of items per page.

        Returns:
        - Dict: A dictionary containing pagination details and data.
        """
        assert index is None or (isinstance(index, int) and index >= 0), "Index must be a non-negative integer."

        # Retrieve the indexed dataset
        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index

        # Gather the data for the requested page
        while len(data) < page_size and next_index < len(indexed_dataset):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }

