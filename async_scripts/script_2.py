import asyncio


async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    # await asyncio.sleep(0.0000001)
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 5000000:
            await asyncio.sleep(0.00000000001)

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    divs1 = asyncio.create_task(find_divisibles(5080000, 34113))
    divs2 = asyncio.create_task(find_divisibles(100052, 3210))
    divs3 = asyncio.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1, divs2, divs3])
    print("ABC")



if __name__ == '__main__':
    asyncio.run(main())