#!/usr/bin/env python3
"""2-measure_runtime.py"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """documented"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    ending = time.time()
    total = ending - start
    return total / n
