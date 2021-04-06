from sys import stdin
from collections import deque

n, l = map(int, stdin.readline().split())
n_list = list(map(int, stdin.readline().rstrip().split()))

mins = deque()

answer_list = list()
for end in range(0, n):
    
    if end-l+1 <= 0:
        start = 0
    else:
        start = end-l+1

    while mins and not (start <= mins[0][1] <= end ):
        mins.popleft()
    
    while mins and mins[-1][0] > n_list[end]:
        mins.pop()

    
    mins.append([n_list[end],end])

    
    answer_list.append(mins[0][0])    

print(*answer_list)