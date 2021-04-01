n = int(input())

data = list()

for i in range(n):
    data.append(input().split())
data = sorted(data, key = lambda x : int(x[0]))

for i in data:
    print(i[0], i[1])