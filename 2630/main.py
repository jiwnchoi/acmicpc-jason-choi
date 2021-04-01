def color_check(paper):
    color = paper[0][0]
    
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] != color:
                return -1
    return color


def dnc(paper, count):
    check = color_check(paper)
    n = len(paper)//2
    if check == 1:
        count[1] += 1
    elif check == 0:
        count[0] += 1
    else:
        dnc([row[0 : n] for row in paper[0 : n]],count)
        dnc([row[n : 2*n] for row in paper[0 : n]],count)
        dnc([row[n : 2*n+1] for row in paper[n : 2*n+1]],count)
        dnc([row[0 : n] for row in paper[n : 2*n+1]],count)


n = int(input())
paper = list()
for i in range(n):
    paper.append(list(map(int,input().split())))

count = [0,0]

dnc(paper,count)

print(count[0])
print(count[1])