from sys import stdin
import heapq


def printmid(leftq, rightq, left_cnt, right_cnt):
    if left_cnt > right_cnt:
        print(-leftq[0])
    elif left_cnt < right_cnt:
        print(rightq[0])
    else:
        print(min(-leftq[0], rightq[0]))



left_cnt = 0
right_cnt = 0

leftq = list()
rightq = list()

n = int(stdin.readline())

for _ in range(n):
    input_number = int(stdin.readline())

    if right_cnt == left_cnt == 0:
        heapq.heappush(rightq, input_number)
        right_cnt += 1

    elif left_cnt == right_cnt or left_cnt > right_cnt:
        left_max = -heapq.heappop(leftq)
        heapq.heappush(rightq, max(left_max, input_number))
        heapq.heappush(leftq, -min(left_max, input_number))
        right_cnt += 1

    elif left_cnt < right_cnt:
        right_min = heapq.heappop(rightq)
        heapq.heappush(leftq, -min(right_min, input_number))
        heapq.heappush(rightq, max(right_min, input_number))
        left_cnt += 1

    printmid(leftq, rightq, left_cnt, right_cnt)
