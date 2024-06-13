#!/usr/bin/env python3
"""Wait Random Time"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    max_delay: the max delay the function gonna wait

    return: the delay time
    """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
