import sys

def mod_multiple(a,b, c):
    return ((a%c) * (b%c))%c

def dnc(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 1:
        return mod_multiple(a, dnc(a**2, b//2, c), c)
    else:
        return dnc(a**2, b//2 , c)
a, b, c = list(map(int, sys.stdin.readline().split()))
print(dnc(a,b,c)%c)