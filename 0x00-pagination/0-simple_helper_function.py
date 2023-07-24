#!/usr/bin/env python3
''' Pagination helper function.on
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''  function that takes two integer arguments page and page_size
    '''
    return ((page - 1) * page_size, page * page_size)
