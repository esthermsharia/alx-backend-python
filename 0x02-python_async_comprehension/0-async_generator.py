#!/usr/bin/env python3
"""Module defines a coroutine that loops asynchronously.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops asynchronously ten times waiting for 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
