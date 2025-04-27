#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""


import asyncio
from typing import List
from bisect import insort

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """documented"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        insort(delays, delay)

    return delays
