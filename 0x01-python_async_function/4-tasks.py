#!/usr/bin/env python3
""" asynchronous coroutine """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Async function that calls task_wait_random n number of times """
    task_list: List = []
    complete_list: List[float] = []

    for x in range(n):
        task_list.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(task_list):
        completed: float = await task
        complete_list.append(completed)

    return (complete_list)
