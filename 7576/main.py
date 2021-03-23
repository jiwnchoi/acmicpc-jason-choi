from collections import deque
from sys import stdin, stdout

m, n = map(int, input().split())

tomatoes = []

q = deque()

for i in range(n):
    tomatoes.append(list(map(int,input().split())))
    for j in range(m):
        if tomatoes[i][j] == 1:
            q.append([i,j])
            
cnt = -1
while q:
    nq = deque()
    while q:
        currunt_tomato = q.popleft()
        y, x = currunt_tomato
        
        if y > 0 and tomatoes[y-1][x] == 0:
            tomatoes[y-1][x] = 1
            nq.append([y-1,x])
            
        if x > 0 and tomatoes[y][x-1] == 0:
            tomatoes[y][x-1] = 1
            nq.append([y,x-1])
            
        if y < n-1 and tomatoes[y+1][x] == 0:
            tomatoes[y+1][x] = 1
            nq.append([y+1,x])
            
        if x < m-1 and tomatoes[y][x+1] == 0:
            tomatoes[y][x+1] = 1
            nq.append([y,x+1])
    q = nq
    cnt +=1 

for t in tomatoes:
    if cnt == -1:
        break
    for tt in t:
        if tt == 0:
            cnt = -1
            break
print(cnt)
    