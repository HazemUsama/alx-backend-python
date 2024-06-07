#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier: float number

    return: a function that multiple `multiplier` with another float
    """
    def multiple(num: float) -> float:
        return num * multiplier
    
    return multiple
