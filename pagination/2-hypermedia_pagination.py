#!/usr/bin/env python3
""" Task 2: Hypermedia pagination """
import csv
import math
from typing import List, Dict, Any

index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads the dataset from the CSV file, caching it after the first load."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page from the dataset.

        Args:
        - page (int): The page number to retrieve.
        - page_size (int): The number of items per page.

        Returns:
        - List of lists: The data for the requested page.
        """
        assert isinstance(page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)

        # If start index exceeds dataset length, return an empty list
        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves a page from the dataset and provides pagination information.

        Args:
        - page (int): The page number to retrieve.
        - page_size (int): The number of items per page.

        Returns:
        - Dict: A dictionary containing pagination information.
        """
        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)
        page_data = self.get_page(page, page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

