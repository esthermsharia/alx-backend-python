#!/usr/bin/env python3
"""Defines a type annotated function that takes a string k
   and an int OR a float v as arguments and returns a tuple.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and a float/integer and returns a tuple"""
    return (k, v * v)
