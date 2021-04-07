# simple
# def simple_coroutine():
#     print("coroutine has been started!")
#     while True:
#         x = yield "foo"
#         print("coroutine received: ", x)
     
 
# cr = simple_coroutine()
# print(next(cr)) # this to start coroutine

# print(cr.send("abc"))  # this send data to couroutine and get it back
# print(cr.send("dfg"))

# counter with send
def count(firstval=0, step=1):
    x = firstval
    while True:
        count_step = yield x
        x += count_step
        
counter = count() # count will start with 0
next(counter)
for i in range(10):
    print(counter.send(2), end=", ")