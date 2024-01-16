#!/usr/bin/env python3
""" asynchronous coroutine """
from typing import List
from time import time
from asyncio import gather
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure total runtime of coroutine """
    start: float = time()
    await gather(async_comp(), async_comp(), async_comp(), async_comp())
    end: float = time()
    return (end - start)
