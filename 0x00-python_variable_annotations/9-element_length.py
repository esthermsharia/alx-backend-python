#!/usr/bin/env python3
"""Defines a function that takes a list and returns a list of iterables"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Demostrates duck-typing """
    return [(i, len(i)) for i in lst]
