from collections import deque
n = int(input())

schedules = list()

for i in range(n):
    schedules.append(list(map(int,input().split())))

schedules = sorted(schedules, key=lambda x : x[1] * (2**32) + x[0])
cnt = 1
lastSchedule = schedules.pop(0)
while(schedules):
    nextSchedule = schedules.pop(0)
    if nextSchedule[0] < lastSchedule[1]:
        continue
    else:
        cnt +=1
        lastSchedule = nextSchedule
        
print(cnt)
    