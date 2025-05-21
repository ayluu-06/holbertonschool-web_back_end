#!/usr/bin/env python3
"""module documented
"""

import csv
import math
from typing import List, Dict, Tuple


def index_range(page, page_size):
    """documented"""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """documented"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: row for i, row in enumerate(dataset)
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """documented"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """documented"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """documented"""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        sorted_keys = sorted(indexed_data.keys())

        assert index in sorted_keys, "Index out of bounds"

        current_idx = sorted_keys.index(index)
        page_data = []
        i = current_idx

        while len(page_data) < page_size and i < len(sorted_keys):
            key = sorted_keys[i]
            page_data.append(indexed_data[key])
            i += 1

        next_index = sorted_keys[i] if i < len(sorted_keys) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data
        }
