#!/usr/bin/python3
"""Defines a functions that annotates the return values."""

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns list element at 0 if list is not empty else returns None"""
    if lst:
        return lst[0]
    else:
        return None
