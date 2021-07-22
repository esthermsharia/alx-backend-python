#!/usr/bin/env python3
"""Defines a type annotated function that takes a list of floats as argument
   and returns their surm as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums up all list items and returns their sum as a float"""
    return sum(input_list)
