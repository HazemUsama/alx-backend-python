#!/usr/bin/env python3
"""Wait Random Time"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """
    max_delay: the max delay the function gonna wait

    return: the delay time
    """
    time = max_delay * random.random()
    await asyncio.sleep(max_delay * random.random())
    return time
