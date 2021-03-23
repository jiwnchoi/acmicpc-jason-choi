import sys
import math as m

def find_push_index(list, value):
    
    start = 0
    end = len(list)-1


    while start < end:
        mid = (start + end) // 2
        if list[mid] >= value:
            end = mid
        else:
            start = mid+1
    
    return end

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

length = [None for i in range(len(numbers))]

maxvalue = [-m.inf]



for i in range(n):
    
    if maxvalue[-1] < numbers[i]:
        maxvalue.append(numbers[i])
        length[i] = len(maxvalue)-1
    elif maxvalue[-1] == numbers[i]:
        length[i] = len(maxvalue)-1
    else:
        tmp = find_push_index(maxvalue, numbers[i])
        length[i] = tmp
        maxvalue[tmp] = numbers[i]



maxlength = len(maxvalue) -1
print(maxlength)
lis = []
i = -1
while maxlength:
    if length[i] == maxlength:
        lis.append(numbers[i])
        maxlength -= 1
    i -=1
        

while len(lis) != 1:
    print(lis.pop(), end=" ")
print(lis[0])