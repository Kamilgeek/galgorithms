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
ind2 = -1
for i in array:
    ind += 1
    if i > max_:
        indmax = ind - 1
        max_ = i
    if i < min_:
        indmin = ind - 1
        min_ = i
sumint = 0
for n in array:
    ind2 += 1
    if ind2 > indmin and ind2 < indmax:
        sumint += n
    elif ind2 < indmin and ind2 > indmax:
        sumint += n
print(f'maxind={indmax}')
print(f'minind={indmin}')
print(f'max = {max_}')
print(f'min = {min_}')
print(f'Сумма ={sumint}')
# Выдает ноль когда минимальное и максимальное число впритык с друг другом так как между ними нет чисел