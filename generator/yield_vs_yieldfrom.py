# For simple iterators, yield from iterable is essentially just a shortened form of for item in iterable: yield item:

def yield_gen():
    yield "BYE"

def yield_from_gen():
    yield from "BYE"

for i in yield_gen():
    print(i)

print(yield_gen())
print(yield_from_gen())
print("-----------")
for i in yield_from_gen():
    print(i)