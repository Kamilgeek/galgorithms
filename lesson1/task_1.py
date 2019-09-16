num = int(input('Введите трехзначное число'))
a = num // 100
b = num // 10 % 10
c = num % 10
sum = a + b + c
com = a * b * c
print(f'сумма ={sum}')
print(f'произведение ={com}')
