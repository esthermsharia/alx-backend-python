#!/usr/bin/env python3
"""Defines a function that takes a float multiplier as an argument and
   returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a multiplier"""
    return (lambda x: x * multiplier)
