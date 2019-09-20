def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n



def rav(n):
    if fact(n) == n*(n+1)/2:
        print('равенство выполняется!')
    else:
        print('равенство не выполняется!')

rav(3)
# 