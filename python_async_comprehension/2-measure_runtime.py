#!/usr/bin/env python3
"""2-measure_runtime.py"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """decumented"""
    start = time.time()

    tasks = []

    for _ in range(4):
        tasks.append(async_comprehension())

    await asyncio.gather(*tasks)

    done = time.time()
    result = done - start
    return result
