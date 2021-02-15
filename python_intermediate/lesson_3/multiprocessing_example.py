import concurrent.futures
from functools import reduce
from time import time


def factorial(n):
    if n in [0, 1]:
        return n
    return reduce(lambda a, b: a * b, range(1, n + 1))


start = time()
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    r = executor.map(factorial, range(50000, 100000, 10000))
print("Multi Finished in", time() - start)
start = time()
for n in range(50000, 100000, 10000):
    factorial(n)
print("Finished in", time() - start)
