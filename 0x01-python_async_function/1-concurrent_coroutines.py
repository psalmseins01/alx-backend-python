#!/usr/bin/env python3
"""Module that execute multiple coroutines at
 the same time with async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
            n - the number of times to spawn max_delays
            max_delay - upper bound of the delays
        Return: A list of float elements
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
