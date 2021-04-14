from sys import stdin
input = stdin.readline().rstrip

n, m = input().split()

r_coordinate = [None, None]
b_coordinate = [None, None]
goal_coordinate = [None, None]

board = list()

for y in range(n):
    tmp = list(input())
    if "B" in tmp:
        b_coordinate = [tmp.index("B"),y]
    if "R" in tmp:
        r_coordinate = [tmp.index("R"), y]
    if "O" in tmp:
        goal_coordinate = [tmp.index("O"), y]

    board.append(tmp)



