#!/usr/bin/env python3
""" asynchronous coroutine """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    async coroutine that waits for a random delay between 0 and max_delay
    """
    random: float = uniform(0, max_delay)
    await asyncio.sleep(random)
    return random
