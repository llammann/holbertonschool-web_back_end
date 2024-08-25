#!/usr/bin/env python3
""" Task 1: Simple pagination """
import csv
from typing import List

# Importing index_range function
index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes an instance of the Server class."""
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Loads and caches the dataset if not already cached."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Retrieves a specific page of the dataset.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            List[List[str]]: The data for the requested page.
        """
        # Validate input arguments
        assert isinstance(page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        all_data = self.dataset()
        page_data = []

        # Calculate the range of data to return
        range_end = page * page_size
        if range_end > len(all_data):
            return page_data  # Return an empty list if the range is out of bounds

        # Get the data within the calculated range
        start_idx, end_idx = index_range(page, page_size)
        for i in range(start_idx, end_idx):
            page_data.append(all_data[i])

        return page_data

