#!/usr/bin/env python3
""" Task 1: Simple pagination """
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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

