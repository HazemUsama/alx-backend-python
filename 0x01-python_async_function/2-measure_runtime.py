#!/usr/bin/env python3
"""Wait N Random Time and measure the avg"""
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    n: the number of random times we are gonna generate
    max_delay: the max delay the function gonna wait

    return: the avg time waited for each call
    """
    start = time()
    waited = asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
