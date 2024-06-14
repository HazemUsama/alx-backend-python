#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Float] 
    """
    collect 10 random numbers using an async comprehensing
    over async_generator
    """
    ans = [n async for n in async_generator()]
    return ans