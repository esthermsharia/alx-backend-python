#!/usr/bin/env python3
"""
   Defines a function that runs a task four times in parallel
   and calculates the runtime.
"""

import asyncio
from typing import List
from time import perf_counter


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes four tasks in parallel and calculates their runtime
    """
    i = perf_counter()
    task = [asyncio.create_task(async_comprehension()) for j in range(4)]
    await asyncio.gather(*task)
    elapsed_time = perf_counter() - i
    return elapsed_time
