#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    dct: a map
    key: key of any value
    default: a variable of type T or none

    return: any type of type T
    """
    if key in dct:
        return dct[key]
    else:
        return default
