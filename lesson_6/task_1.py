import random
import sys
from memory_profiler import memory_usage
att = 0
b = random.randint(1, 100)
print(b)
while att < 10:
    num = int(input('Загадайте число от 1-100'))
    if b == num:
        print('Вы угадали!')
        att +=11
    elif  b > num:
        print('Вы ввеоли слишком маленькое число!')
        att+=1
    else:
        print('Вы ввели слишком большое число!')
        att+=1

if att == 10:
    print(f'Число попыток дошло до 10 , загаданное число равнялось{b}')

print(sys.getsizeof(att))
print(sys.getsizeof(b))
print(sys.getsizeof(num))
print(f'скрипт занял памяти{memory_usage()}')
# ответ -  под переменные было выделено 86 байт