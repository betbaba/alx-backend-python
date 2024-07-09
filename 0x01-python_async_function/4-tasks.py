#!/usr/bin/env python3
"""task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Awaits tasks and return the list of time it waits"""
    delays = [task_wait_random(max_delay) for i in range(n)]
    all_delays = await asyncio.gather(*delays)
    return sorted(all_delays)
