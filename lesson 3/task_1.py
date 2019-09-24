import random

# SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 10
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
for i in range(2,100):
    if i % 2 == 0:
        two += 1
    if i % 3 == 0:
        three += 1
    if i % 4 == 0:
        four += 1
    if i % 5 == 0:
        five += 1
    if i % 6 == 0:
        six += 1
    if i % 7 == 0:
        seven += 1
    if i % 8 == 0:
        eight += 1
    if i % 9 == 0:
        nine += 1
print(f'на 2 делится{two},/n на 3 делится {three}, на 4 делится {four},'
      f' на 5 делится{five}, на 6 делистя {six}, на 7 делится {seven}, на 8 делится {eight}, на 9 делится {nine}')