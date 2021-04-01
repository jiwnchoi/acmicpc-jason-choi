n = int(input())

data  = list()

for i in range(n):
    data = list(map(int,input().split()))
    w = data[2] // data[0]
    h = data[2] % data[0]
    print("%d%s"%(h,str((w+1)).zfill(2)))

