import asyncio


async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i==0:
            continue
        if i % div_by == 0:
            located.append(i)
        if i% 500000 == 0:
            await asyncio.sleep(0.0001)

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    divs1 = asyncio.create_task(find_divisibles(50800000, 34113))
    divs2 = asyncio.create_task(find_divisibles(100052, 3210))
    divs3 = asyncio.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1, divs2, divs3])


if __name__ == '__main__':
    asyncio.run(main())