#!/usr/bin/env python3
""" Task 0: Simple helper function for pagination """

def index_range(page_number: int, size_per_page: int) -> tuple:
    """ 
    Calculate start and end indexes for a given page and page size.

    Args:
    - page_number (int): The current page number (1-indexed).
    - size_per_page (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start and end indexes.
    """
    start_idx = (page_number - 1) * size_per_page
    end_idx = page_number * size_per_page
    return (start_idx, end_idx)

