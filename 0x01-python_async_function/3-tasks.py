#!/usr/bin/env python3
"""Create a Task"""
from asyncio import create_task, Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    max_delay: the max delay the function gonna wait

    return: asyncio.Task
    """
    return create_task(wait_random(max_delay))
