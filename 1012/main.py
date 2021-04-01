import sys
sys.setrecursionlimit(10000)




def dfs(farm, x,y):
    mx = len(farm[0])
    my = len(farm)
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < mx and 0 <= ny < my :
            if farm[ny][nx] == 1:
                farm[ny][nx] = 0
                dfs(farm,nx,ny)
                

n = int(input())
for _ in range(n):
    m,n,k = map(int,input().split())
    farm = [[0] * m for i in range(n)]
    visited = farm[:]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if farm[i][j]:
                dfs(farm, j,i)
                cnt += 1
                
                
    print(cnt)