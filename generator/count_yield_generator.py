def count(firstval=0, step=1):
    x = firstval
    while True:
        yield x
        x += step
        
counter = count() # count will start with 0
for i in range(10):
    print(next(counter), end=", ")