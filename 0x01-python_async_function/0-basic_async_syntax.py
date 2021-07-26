#!/usr/bin/env python3
"""Module defines a function that waits for a random delay
   time, then returns a random number
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay between 0 and max_delay and
    returns the value of the random number.
    """
    random_num = random.random() * max_delay
    return random_num
