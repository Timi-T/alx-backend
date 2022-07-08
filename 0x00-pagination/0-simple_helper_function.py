#!/usr/bin/env python3
"""
Module for simple helper function for pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Helper function for pagination"""
    start = (page_size * page) - page_size
    end = start + page_size
    return (start, end)
