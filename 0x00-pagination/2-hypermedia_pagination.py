#!/usr/bin/env python3
"""pagination module"""
from typing import List, Dict, Any
import csv
import math
index_range = __import__('0-simple_helper_function').index_range


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
        """Returns page of the dataset"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset) or start_index >= end_index:
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        page_data = self.get_page(page, page_size)
        page_size = len(page_data)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        hyper_data = {
            "page_size": f"{page_size}",
            "page": f"{page}",
            "data": f"{page_data}",
            "next_page": f"{page + 1}" if page < total_pages else None,
            "prev_pages": f"{page - 1}" if page > 1 else None,
            "total_pages": f"{total_pages}"
        }

        return hyper_data
