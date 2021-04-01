from collections import Counter

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
find = list(map(int, input().split()))

c = Counter(cards)
for i in range(m-1):
    print(c[find[i]], end=" ")
print(c[find[m-1]], end="")