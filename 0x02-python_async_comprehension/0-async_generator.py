#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import sleep
from typing import Generator
from random import random


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        await sleep(1)
        yield random(0, 10)
