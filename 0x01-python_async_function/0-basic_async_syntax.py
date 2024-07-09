#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument
   and returns a float
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay"""
    time_delay = random.uniform(0, max_delay)
    await asyncio.sleep(time_delay)
    return time_delay
