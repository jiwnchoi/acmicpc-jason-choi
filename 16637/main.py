import sys
from itertools import product
from math import inf

def calc(a, b, c):
    if b == "+" : 
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    
def calc_expression(e):
    while len(e) > 1:
        e[0] = calc(e[0],e[1],e[2])
        e = [e[0]] + e[3:]
    return e[0]


def dfs(e, answer):
    calc(e[0], e[1], dfs(e[2:],0))
    calc(calc(e[0], e[1], e[2]),e[3],dfs(e[4:],0))


n = int(sys.stdin.readline().rstrip())


e = list(sys.stdin.readline().rstrip())

for i in range(len(e)):
    if '0'<= e[i] <= '9':
        e[i] = int(e[i])

ne = n // 2
nn = n // 2 + 1

expression_list = list(map(list,product([0,1], repeat=ne)))
i = 0
while (i < len(expression_list)):
    for j in range(1, ne):
       if expression_list[i][j] and expression_list[i][j-1]:
           del(expression_list[i])
           i -=1
    i += 1


ans = -inf

for expression in expression_list:
    tmp = e[:]
    i = 0
    while i < ne and i < len(expression):
        if expression[i]:
            tmp[2* i] = calc(tmp[2*i], tmp[2*i+1], tmp[2*i+2])
            del(tmp[2*i+1])
            del(tmp[2*i+1])
            del(expression[i])
            i -= 1
        i+=1
    ans = max(ans, calc_expression(tmp))

print(ans)