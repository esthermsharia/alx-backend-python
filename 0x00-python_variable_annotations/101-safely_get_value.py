#!/usr/bin/env python3
""" Defines a function that returns a value from a dictionary if
    the supplied key is found
"""

from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Return a key if found in dict else return None """
    if key in dct:
        return dct[key]
    else:
        return default
