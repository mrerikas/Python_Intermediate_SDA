import timeit

setup = """
from random import  randint

numbers = [randint(1, 256) for _ in range(100_000)]
"""

code1 = """
histogram = {}
for n in numbers:
    if n in histogram:
        histogram[n] += 1
    else:
        histogram[n] = 1
"""

code2 = """
histogram = {}
for n in numbers:
    try:
        histogram[n] += 1
    except KeyError:
        histogram[n] = 1
"""

print(timeit.timeit(stmt=code1, setup=setup, number=10))
print(timeit.timeit(stmt=code2, setup=setup, number=10))
