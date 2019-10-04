import random
import sys
from memory_profiler import memory_usage

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = float("inf")
indmin = 0
min2 = float("inf")
indmin2 = 0
ind = 0

for i in array:
    ind += 1
    if i < min_:
        indmin = ind - 1
        min_ = i
    if i < min2 and i >= min_:
        indmin2 = ind -1
        if indmin2 != indmin:
            min2 = i

print(f'minind={indmin}')
print(f'minind2={indmin2}')
print(f'min = {min_}')
print(f'min2 = {min2}')

print(sys.getsizeof(SIZE))
print(sys.getsizeof(MIN_ITEM))
print(sys.getsizeof(MAX_ITEM))
print(sys.getsizeof(indmin))
print(sys.getsizeof(min_))
print(sys.getsizeof(min2))
print(sys.getsizeof(indmin2))
print(sys.getsizeof(ind))
print(f'скрипт занял памяти{memory_usage()}')
# ответ - под переменные было выделено 224 байт
