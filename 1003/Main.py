def pibo(piboMemo, n):
    if(piboMemo[n] is not None):
        return piboMemo[n]
    else:
        piboMemo[n] = pibo(piboMemo, n-1) + pibo(piboMemo,n-2)
        return piboMemo[n]


piboMemo = [None for _ in range(41)]
piboMemo[0] = 0
piboMemo[1] = 1

caseNumber = int(input())

for _ in range(caseNumber):
    tmp = int(input())
    if(tmp == 0):
        print(1,0)
    else:
        print(pibo(piboMemo,tmp-1),pibo(piboMemo,tmp))




