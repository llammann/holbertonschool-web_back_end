#!/usr/bin/env python3
""" Task 0. Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """  The coroutine loop 10 times, async wait 1 second, yield a random num in 0-10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        
        
