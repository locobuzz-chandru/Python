# Asynchronous programming-> is a type of parallel programming in which a unit of work is allowed to run separately from
# the primary application thread. When the work is complete, it notifies the main thread about completion or failure of
# the worker thread.

# Asynchronous is a non-blocking architecture, so the execution of one task isn't dependent on another.
# Tasks can run simultaneously.

# Synchronous is a blocking architecture, so the execution of each operation is dependent on the completion of the one
# before it

# Iterators-> are objects that allow the traversal of iterables. They often have return values at their end
# Generators-> are functions that allow un-continuous execution. Only run when the next value is needed
# aiter()-> function returns an asynchronous iterator for an asynchronous iterable
# __anext__()-> returns the next element (awaitable)

# coroutine-> is a function that can suspend its execution before reaching return,
# and it can indirectly pass control to another coroutine for some time
# A function that we introduce with async def is a coroutine. It may use await, return, or yield
# Using await and/or return creates a coroutine function. To call a coroutine function, we must await it
import asyncio


class AsyncIterator:
    def __init__(self):
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= 10:
            raise StopAsyncIteration
        self.counter += 1
        await asyncio.sleep(1)
        return self.counter


async def main():
    it = AsyncIterator()
    awaitable = anext(it)
    result = await awaitable
    print(result)


asyncio.run(main())
