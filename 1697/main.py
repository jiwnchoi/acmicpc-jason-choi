from collections import deque
import sys

maxposition = 100001

n, k = map(int,input().split())
visited = [None for _ in range(maxposition)]
q = deque()
q.append(n)
visited[n] = 0
while q:
    t = q.popleft()
    if t == k:
        print(visited[t])
        break
    if(0<= t-1 < maxposition):
        if((visited[t-1] == None or visited[t-1] > visited[t]+1)):
            q.append(t-1)
            visited[t-1] = visited[t] +1 
    if( 0<= t+1 < maxposition):
        if((visited[t+1] == None or visited[t+1] > visited[t]+1)):
            q.append(t+1)
            visited[t+1] = visited[t] +1
    if(0<= 2*t < maxposition):
        if((visited[2*t] == None or visited[2*t] > visited[t]+1)):
            q.append(2*t)
            visited[2*t] = visited[t] +1