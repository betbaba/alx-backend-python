#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list which takes
   a list mxd_lst of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Takes mxd_lst of integers and floats
       and returns their sum as a float
    """
    total: float = 0.0
    for i in mxd_list:
        total += i
    return total
