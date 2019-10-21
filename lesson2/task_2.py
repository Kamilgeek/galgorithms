num = int(input('Введите число'))

chet = 0
nechet = 0

while num > 0:
    if num % 2 == 0:
        chet += 1
    else:
        nechet += 1
    num = num // 10

print(f'четных = {chet}, нечетных = {nechet}')

# def chet(n):
#     chet = 0
#     nechet = 0
#     if n < 0:
#         return chet, nechet
#     else:
#         if n % 2 ==0:
#             chet+=1
#         else:
#             nechet+=1
#     return chet(n//10)
#
# print(chet(252))
#