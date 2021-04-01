input()
n = list(map(int, input().split()))

primeList = [n for n in range(2,1001)]


for i in primeList:
    for j in primeList:
        if(j % i == 0 and j != i):
            primeList.remove(j)
count = 0

for i in n:
    if i in primeList:
        count+=1
        
print(count)