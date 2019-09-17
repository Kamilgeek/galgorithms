print('Введите три стороны треугольника')
a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))

if a + c <= b or a + b <= c or b + c <= a:
    print('Треугольника не существует!')
elif a != b and b != c and c != a:
    print('Треугольник разносторонний!')
elif a==b==c:
    print('Треугольник равносторонний!')
else:
    print('Треугольник равнобедрянный!')