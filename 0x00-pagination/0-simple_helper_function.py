#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for a given pagination parameters.
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        tuple: A tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
