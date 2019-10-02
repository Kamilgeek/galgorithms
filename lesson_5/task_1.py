from collections import Counter

# Rally = {'1kv':int(input('введите прибыль за 1 квартал')),
#           '2kv': int(input('введите прибыль за 2 квартал')),
#           '3kv':int(input('введите прибыль за 3 квартал')),
#           '4kv':int(input('введите прибыль за 4 квартал'))}

Rally = Counter(kv1 =int(input('введите прибыль за 1 квартал для Rally')),
                kv2 =int(input('введите прибыль за 2 квартал для Rally')),
                kv3 =int(input('введите прибыль за 3 квартал для Rally')),
                kv4 =int(input('введите прибыль за 4 квартал для Rally')))



Shmally = Counter(kv1 =int(input('введите прибыль за 1 квартал для Shmally')),
                kv2 =int(input('введите прибыль за 2 квартал для Shmally')),
                kv3 =int(input('введите прибыль за 3 квартал для Shmally')),
                kv4 =int(input('введите прибыль за 4 квартал для Shmally')))

Ukrally = Counter(kv1 =int(input('введите прибыль за 1 квартал для Ukrally')),
                kv2 =int(input('введите прибыль за 2 квартал для Ukrally')),
                kv3 =int(input('введите прибыль за 3 квартал для Ukrally')),
                kv4 =int(input('введите прибыль за 4 квартал для Ukrally')))

midRally =(sum(Rally.values())/4)
midShmally = (sum(Shmally.values())/4)
midUkrally = (sum(Ukrally.values())/4)

thecompanys = [midRally, midShmally, midUkrally]

maxcompany = max(thecompanys)
mincompany = min(thecompanys)
num = -1
for i in thecompanys:
    num += 1
    if i == maxcompany:
        if num == 0:
            print('среднее максимальное у компании Rally')
        if num == 1:
            print('среднее максимальное у компании Shmally')
        if num == 2:
            print('среднее максимальное у компании Ukrally')
    if i == mincompany:
        if num == 0:
            print('среднее минимальное у компании Rally')
        if num == 1:
            print('среднее минимальное у компании Shmally')
        if num == 2:
            print('среднее минимальное у компании Ukrally')



