def check(w):
    tmp = []
    checker = 0
    for ww in w:
        if checker < 0:
            print("NO")
            return 0
        if(ww == "("):
            checker += 1
        else:
            checker -= 1
    if(checker == 0):
        print("YES")
        return 1
    else:
        print("NO")
        return 0

n = int(input())

for i in range(n):
    check(input())