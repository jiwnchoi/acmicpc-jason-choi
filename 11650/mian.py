coordinates = list()

n = int(input())
for i in range(n):
    coordinates.append(list(map(int,input().split())))

coordinates = sorted(coordinates,key=lambda x : x[0] * 10000000 + x[1])

for i in range(n):
    print("%d %d"%(coordinates[i][0], coordinates[i][1]))