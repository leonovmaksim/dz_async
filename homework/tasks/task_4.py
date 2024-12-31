import asyncio


async def task_1(i: int, order: list):
    order.append(1)
    if i == 0:
        return

    if i > 5:
        await task_2(i // 2, order)
    else:
        await task_2(i - 1, order)


async def task_2(i: int, order: list):
    order.append(2)
    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2, order)
    else:
        await task_2(i - 1, order)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212
    order = []
    cor = task_1(i, order)
    task = asyncio.create_task(cor)
    await task # task_1(i)
    return int(''.join(map(str, order)))
    # YOUR CODE GOES HERE
