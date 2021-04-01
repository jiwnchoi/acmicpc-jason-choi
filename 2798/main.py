from itertools import permutations as p
n, m = map(int, input().split())
numbers = map(int,input().split())

summ = 0
pers = p(numbers,3)

for per in pers:
    ss = sum(per)
    if (ss > m):
        continue
    if(m-ss < m-summ):
        summ = ss
    
print(summ)