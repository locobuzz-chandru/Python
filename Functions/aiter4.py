import asyncio


class AsyncIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __aiter__(self):
        self.cur = self.start
        return self

    async def __anext__(self):
        await asyncio.sleep(1)
        if self.cur >= self.stop:
            raise StopAsyncIteration

        self.cur += 1
        return self.cur - 1


async def example():
    obj = AsyncIterator(1, 10)
    obj_iter = aiter(obj)
    async for num in obj_iter:
        print(num)


asyncio.run(example())
