n, r, c = map(int, input().split())

count = 0



def func(count, n, r, c):
    n2 = (2 ** n)**2
    if n == 1:
        if r >= 1:
            if c >= 1:
                count += 3
            else:
                count +=2
        else:
            if c >= 1:
                count +=1
        return count
    else:
        if r >= (2**(n-1)):
            if c >= (2**(n-1)):
                count += 3 * n2 / 4
                r -= (2**(n-1))
                c -= (2**(n-1))
            else:
                count += n2/2
                r -= (2**(n-1))
        else:
            if c >= (2**(n-1)):
                count += n2 / 4
                c -= (2**(n-1))
        return func(count, n-1, r, c)



print(int(func(count,n,r,c)))