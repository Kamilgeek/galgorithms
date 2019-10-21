import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

index = []
ind = 0
for i in array:
    ind += 1
    if i % 2 == 0:
        index.append(ind-1)

print(index)