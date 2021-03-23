import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
pal = [[None for _ in range(n)] for j in range(n+1)]
pal[0] = None
pal[1] = [1 for _ in range(n)]


for i in range(n-1):
    if numbers[i] == numbers[i+1]:
        pal[2][i] = 1
    else:
        pal[2][i] = 0

for i in range(3, n+1):
    mid = (i-1)//2
    if i%2 == 1:
        for j in range(n-i+1):
            if pal[i-2][mid+j] and numbers[j] == numbers[j+mid*2]:
                pal[i][j+mid] = 1
            else:
                pal[i][j+mid] = 0 
    
    else:
        for j in range(n-i+1):
            if pal[i-2][mid+j] and numbers[j] == numbers[j+mid*2+1]:
                pal[i][j+mid] = 1
            else:
                pal[i][j+mid] = 0



m = int(sys.stdin.readline())
for i in range(m):
    start, end = map(int,sys.stdin.readline().split())
    print(pal[end-start+1][((start+end)//2)-1])
