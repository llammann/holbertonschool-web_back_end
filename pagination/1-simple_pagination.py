#!/usr/bin/env python3
""" Task 1: Simple pagination """
import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"


    def __init__(self) -> None:
        """Initializes a Server instance."""
        self.__dataset: List[List] = []


    def dataset(self) -> List[List]:
        """Loads the dataset from the CSV file, caching it after the first load."""
        if not self.__dataset:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]  # Skip the header row

        return self.__dataset


   def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
    """Finds indexes to paginate and returns the corresponding pages."""
    assert isinstance(page, int) and page > 0, "Page number must be a positive integer."
    assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

    all_of_data = self.dataset()
    start_idx, end_idx = index_range(page, page_size)
    
    return all_of_data[start_idx:end_idx]

