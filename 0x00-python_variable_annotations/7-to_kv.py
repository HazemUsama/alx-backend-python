#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    k: string
    v: value

    return: (k, v^hello1)
    """
    return (k, v**2)
