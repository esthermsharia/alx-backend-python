#!/usr/bin/env python3
"""Defines a function that takes in a mixed list of integers and floats
   and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of integers and floats and returns the sum"""
    return sum(mxd_lst)
