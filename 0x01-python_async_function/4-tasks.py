#!/usr/bin/env python3
"""Wait N Random Time but with a twist"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n: the number of random times we are gonna generate
    max_delay: the max delay the function gonna wait

    return: a list of random times we waited
    """
    waited = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(waited)]
