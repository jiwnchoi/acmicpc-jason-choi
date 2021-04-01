def fac(n):
    if( n == 1 ):
        return 1
    else:
        return fac(n-1) * n

n, k = list(map(int, input().split()))

print(int(fac(n)/(fac(k) * fac(n-k))))