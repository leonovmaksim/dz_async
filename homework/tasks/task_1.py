import asyncio
from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        f = f()
        task = asyncio.create_task(f)
        result = await task
        return result
    elif isinstance(f, Task):
        result = await f
        return result
    elif isinstance(f, Coroutine):
        task = asyncio.create_task(f)
        result = await task
        return result
    else:
        raise ValueError('invalid argument')
