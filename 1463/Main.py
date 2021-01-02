def nextStep(step):
    dp = []
    for i in step:
        if(i%3 == 0):
            dp.append(i//3)
        if(i%2 == 0):
            dp.append(i//2)
        dp.append(i-1)
    return dp


dp = []
dp.append([int(input())])

cnt = 0

while True:
    if(1 in dp[cnt]):
        print(cnt)
        break
    else:
        dp.append(nextStep(dp[cnt]))
        cnt+=1