import asyncio

# async def find_divisibles(inrange, div_by):
#     print("finding nums in range {} divisible by {}".format(inrange, div_by))
#     located = []
#     for i in range(inrange):
#         if i % div_by == 0:
#             located.append(i)
#         if i % 50000 == 0:
#             await asyncio.sleep(0.0001)

#     print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
#     return located

async def end(id):
    print("End: "+id)
    await asyncio.sleep(0)
    
    print("After end: "+id)
    return 30

async def fn_seq(id):
    print("start it "+id)
    await end(id+"_1")
    await end(id+"_2")
    # a2=asyncio.create_task(end(id+"_1"))
    # a3=asyncio.create_task(end(id+"_2"))
    # await asyncio.wait([a2,a3])
    # # await a2
    print("After it "+id)
    return 1

async def main():
    # for i in range(2):
    a=asyncio.create_task(fn_seq("1"))
    b=asyncio.create_task(fn_seq("2"))
    print(a)
    print(b)
    await asyncio.wait([a,b])


if __name__ == "__main__":
    asyncio.run(main())
        # print(d1.result())
    # except Exception as e:
    #     # logging...etc
    #     pass
    # # finally:
    # loop.close()
