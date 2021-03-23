n = int(input())

houses = list()

for _ in range(n):
    houses.append(list(map(int,input().split())))
    
summ = [houses[0][0],houses[0][1],houses[0][2] ]
for i in range(1,len(houses)):
    tmpsumm = summ[:]
    summ[0] = min(tmpsumm[1]+houses[i][0], tmpsumm[2] + houses[i][0])
    summ[1] = min(tmpsumm[2]+houses[i][1], tmpsumm[0] + houses[i][1])
    summ[2] = min(tmpsumm[0]+houses[i][2], tmpsumm[1] + houses[i][2])
print(min(summ))
        