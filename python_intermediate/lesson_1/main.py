from sys import getsizeof
from random import randint
from collections import deque

simple = [randint(1000, 10000) for _ in range(1000000)]
getsizeof(simple)
unique_id = {id(n) for n in simple}
sum([getsizeof(n) for n in simple])
unique_n = set(simple)
cache = {k: k for k in simple}
unique_n_ids = {id(n) for n in unique_n}
unique_n_ids.issubset(unique_n_ids)
len(unique_n_ids.intersection(unique_n_ids))
cache_list = [cache[n] for n in simple]
getsizeof(cache_list)
sum(getsizeof(n) for n in unique_n)
skaiciai = simple = [randint(1, 100) for _ in range(10000)]
histogram = {}
for n in skaiciai:
    histogram[n] = histogram.get(n, 0) + 1
print(set(histogram.values()))
print(max(histogram.values()))
neighbor_histogram = {}
for key in zip(skaiciai[:-1], skaiciai[1:]):
    neighbor_histogram[key] = neighbor_histogram.get(key, 0) + 1
nh = {
    k: v
    for k, v in sorted(neighbor_histogram.items(), key=lambda x: x[1], reverse=True)
}
print(nh)
d = deque([1, 2, 3, 5])
print(d.popleft())
print(d.pop())
# Kvietimų grandinės
v = "verte".count("e").bit_length()
print(v)

