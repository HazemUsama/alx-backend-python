#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    lst: a sequence of any type

    return: an element of the sequence or none
    """
    if lst:
        return lst[0]
    else:
        return None
