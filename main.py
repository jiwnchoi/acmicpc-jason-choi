import sys

def isempty(d):
    if(len(d) == 0):
            return(1)
    else:
        return(0)

from collections import deque

d = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    inp = sys.stdin.readline().split()
    if inp[0] == "push":
        d.append(inp[1])
    elif inp[0] == "top":
        if(isempty(d)):
            print(-1)
        else:
            tmp = d.pop()
            print(tmp)
            d.append(tmp)
    elif inp[0] == "size":
        print(len(d))
    elif inp[0] == "pop":
        if(isempty(d)):
            print(-1)
        else:
            print(d.pop())
    elif inp[0] == "empty":
        print(isempty(d))