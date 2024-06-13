#!/usr/bin/env python3
"""Wait N Random Time"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n: the number of random times we are gonna generate
    max_delay: the max delay the function gonna wait

    return: a list of random times we waited
    """
    waited = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(waited)]



