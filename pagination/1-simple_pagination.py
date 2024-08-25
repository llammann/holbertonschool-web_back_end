#!/usr/bin/env python3
""" Task 1: Simple pagination """
import csv
from typing import List, Tuple

# Import index_range function from the previous task
index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initializes an instance of Server class."""
        self.__dataset: List[List[str]] = None

    def dataset(self) -> List[List[str]]:
        """Loads and caches the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]  # Skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Retrieves a page from the dataset.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            List[List[str]]: The data for the requested page.
        """
        # Validate input types and values
        assert isinstance(page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)

        # Check if the start index is within the bounds of the dataset
        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

