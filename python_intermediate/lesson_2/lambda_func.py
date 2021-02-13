# Map
from functools import reduce

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

map_result = list(map(lambda x: round(x ** 2, 2), my_floats))

filter_result = list(filter(lambda name: len(name) <= 7, my_names))

reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
# reduce(func, iterable[, initial])

a.sort(key=lambda x: x[1])  # sorting list by second item in a tuple.

print(map_result)
print(filter_result)
print(reduce_result)
print(a)
