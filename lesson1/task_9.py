print('enter 3 different numbers')
a =int(input('a ='))
b =int(input('b ='))
c =int(input('c ='))

if c<a<b or b<a<c:
    print(f'middle - a')
elif c<b<a or a<b<c:
    print(f'middle - b')
else:
    print(f'middle - c')