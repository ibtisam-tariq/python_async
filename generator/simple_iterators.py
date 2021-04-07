# Generators are a special kind of function, which enable us to implement or generate iterators.
other_cities = [1,2,3]

# for city in other_cities:
#     print(city)

city_iterator = iter(other_cities)
while True:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        print("END")
        break