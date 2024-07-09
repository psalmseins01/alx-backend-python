#!/usr/bin/env python3
""" Module demonstrating Asycio """

from asyncio import Task
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Using Task type """
    task_wait = asyncio.create_task(wait_random(max_delay))
    return task_wait
