#!/usr/bin/env python3
"""
Module for simple helper function for pagination
"""

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Helper function for pagination"""
    start = (page_size * page) - page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function to get data from a file"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        pages = index_range(page, page_size)
        start = pages[0]
        end = pages[1]
        data = self.dataset()
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function to get details of response"""
        pages = index_range(page, page_size)
        start = pages[0]
        end = pages[1]
        pages_size = end - start
        data = self.get_page(page, pages_size)
        next_page = page + 1
        if next_page > len(data):
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        total_pages = math.ceil(len(self.__dataset) / pages_size)
        return {"page_size": page_size, "page": page, "data": data,
                "next_page": next_page, "prev_page": prev_page,
                "total_pages": total_pages}
