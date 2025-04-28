#!/usr/bin/env python3
"""4-tasks.py"""

import asyncio
from typing import List
from bisect import insort

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """documented"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        insort(delays, delay)

    return delays
