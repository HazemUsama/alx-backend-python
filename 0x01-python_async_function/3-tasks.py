#!/usr/bin/env python3
"""Create a Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    max_delay: the max delay the function gonna wait

    return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
