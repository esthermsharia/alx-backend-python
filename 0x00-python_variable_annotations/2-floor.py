#!/usr/bin/env python3
"""Defines a type annotated functions that takes a float and returns the
   floor value of the float.
"""
import math


def floor(n: float) -> int:
    """Takes a float value and returns the floor value of the float"""
    return math.floor(n)
