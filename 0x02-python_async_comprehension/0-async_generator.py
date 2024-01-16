#!/usr/bin/env python3
""" asynchronous coroutine """

from random import uniform
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loops 10 times while waiting 1 sec asynchronously """
    for x in range(10):
        await sleep(1)
        yield uniform(1, 10)
