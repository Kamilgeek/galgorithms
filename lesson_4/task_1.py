import timeit
import cProfile

def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n



def rav(n):
    if fact(n) == n*(n+1)/2:
        return f'равенство выполняется!'
    else:
        return f'равенство не выполняется!'
# "task_1.rav(5)"
# 100 loops, best of 3: 1.5 usec per loop
# "task_1.rav(50)"
# 100 loops, best of 3: 13.5 usec per loop
# "task_1.rav(500)"
# 100 loops, best of 3: 213 usec per loop
# 10 function calls (5 primitive calls) in 0.000 seconds   -5
# 6/1    0.000    0.000    0.000    0.000 task_1.py:4(fact)  -5
# 55 function calls (5 primitive calls) in 0.000 seconds  -50
#  51/1    0.000    0.000    0.000    0.000 task_1.py:4(fact) -50
# 505 function calls (5 primitive calls) in 0.001 seconds- 500
# 501/1    0.001    0.000    0.001    0.001 task_1.py:4(fact)  -500




def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
def rav2(n):
    if factorial(n) == n*(n+1)/2:
        return f'равенство выполняется!'
    else:
        return f'равенство не выполняется!'

# "task_1.rav2(5)"
# 100 loops, best of 3: 1.04 usec per loop
# "task_1.rav2(50)"
# 100 loops, best of 3: 7.94 usec per loop
# "task_1.rav2(500)"
# 100 loops, best of 3: 152 usec per loop
# 5 function calls in 0.000 seconds -5
# 1    0.000    0.000    0.000    0.000 task_1.py:32(factorial)  - 5
# 5 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:32(factorial)  - 50
# 5 function calls in 0.000 seconds      -500
# 1    0.000    0.000    0.000    0.000 task_1.py:32(factorial)  - 500
cProfile.run("rav2(500)")

# Вывод:
# решение с помощью цикла работает немного быстрее, но зато намного меньше вызовов и меньше занимает
# места чем рекурсивный вариант и мне кажеться оба варианта это O(n)
