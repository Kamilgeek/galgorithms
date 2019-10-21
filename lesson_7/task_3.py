import random

m = random.randint(0, 10)
print(m)
SIZE = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array.sort()
print(array)


def mediana_search(array):
    if len(array) % 2 == 0:
        middle = len(array) // 2
        mediana = (array[middle] + array[middle - 1]) / 2
        return mediana
    else:
        medianaind = (len(array) // 2)
        mediana = array[medianaind]
        return mediana


print(mediana_search(array))

