def inverseMatrix(matrix):
    inversedMatrix = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(inversedMatrix[i][j] == "0"):
                inversedMatrix[i][j] == "1"
            else:
                inversedMatrix[i][j] == "0"
    return inversedMatrix

def countFunc(m1, m2):
    




row, col = input().split(" ")
row = int(row)
col = int(col)

m1 = list()
m2 = list()

for _ in range(row):
    row = list(input())
    m1.append(row)

for _ in range(row):
    row = list(input())
    m2.append(row)

if(len(m1) <= 3 and len(m1[0]) <= 3):
    if(m1 == m2 or m1 == inverseMatrix(m2)):
        print(1)
    else:
        print(-1)

else:
    print(countFunc(m1,m2))