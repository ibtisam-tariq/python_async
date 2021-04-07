def city_generator():
    yield("Hamburg")
    yield("Konstanz")
    return 
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")  

# for i in city_generator():
#     print(i)

x=city_generator() # returns an iterator,  generator object
# print(x)
print(next(x))
# # print x
print(next(x))
# # print x
print(next(x))

# def ff():
#     return "abc"
#     return "cdf"

# print(ff())