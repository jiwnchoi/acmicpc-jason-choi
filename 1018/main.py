n, m = map(int,input().split())

BW = list("BWBWBWBW")
WB = list("WBWBWBWB")

type1 = [BW, WB, BW, WB, BW, WB, BW, WB]
type2 = [WB, BW, WB, BW, WB, BW, WB, BW]



board = list()

for _ in range(n):
    board.append(list(input()))

count = 50 * 50

for startX in range(0,m-7):
    for startY in range(0, n-7):
        n1 = 0
        n2 = 0
        for y in range(startY, startY+8):
            for x in range(startX, startX+8):    
                if board[y][x] != type1[y-startY][x-startX]:
                    n1 += 1
        for y in range(startY, startY+8):
            for x in range(startX, startX+8):  
                if board[y][x] != type2[y-startY][x-startX]:
                    n2 += 1
                    
                    
        count = min(count, n1, n2)
        
print(count)