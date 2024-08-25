#!/usr/bin/env python3
""" Task 1: Simple pagination """
import csv
from typing import List, Tuple, Optional

index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initializes a Server instance."""
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Loads the dataset from the CSV file, caching it after the first load."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Retrieves a page from the dataset.

        Args:
        - page (int): The page number to retrieve.
        - page_size (int): The number of items per page.

        Returns:
        - List of lists: The data for the requested page.
        """
        assert isinstance(page, int), "Page number must be an integer."
        assert page > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int), "Page size must be an integer."
        assert page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

