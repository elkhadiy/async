from asyncio import *

async def countdown(n):
    while n > 0:
        print('Down', n)
        await sleep(4)
        n -= 1

async def countup(stop):
    x = 0
    while x < stop:
        print('Up', x)
        await sleep(1)
        x += 1

async def main():
    await gather(countdown(5), countup(20))

run(main())