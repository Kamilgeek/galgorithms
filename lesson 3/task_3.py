import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = float("inf")
max_ = 0
indmin = 0
indmax = 0
ind = 0
for i in array:
    ind += 1
    if i > max_:
        indmax = ind - 1
        max_ = i
    if i < min_:
        indmin = ind - 1
        min_ = i
array[indmin], array[indmax] = array[indmax], array[indmin]
print(f'maxind={indmax}')
print(f'minind={indmin}')
print(f'max = {max_}')
print(f'min = {min_}')
print(f'Поменяли местами !{array}')