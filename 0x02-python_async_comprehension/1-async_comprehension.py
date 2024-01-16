#!/usr/bin/env python3
""" asynchronous coroutine """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collects 10 random numbers using an async comprehensing """
    return [x async for x in async_generator()]
