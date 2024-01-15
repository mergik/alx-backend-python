#!/usr/bin/env python3
""" Type-annotated function returns asynchronous coroutine """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns task that takes random amount of time """
    return asyncio.create_task(wait_random(max_delay))
