def solution(bridge_length, weight, truck_weights):
    time = 0
    end = list()
    going = list()
    waiting = list()
    going_weight = 0
    tmp = 0
    for truck in truck_weights:
        waiting.append([truck,1])
    
    while waiting != [] or going != []:
        time += 1


        i=0
        while i < len(going):
            going[i][1] += 1
            if going[i][1] > bridge_length:
                going_weight -= going[i][0]
                del(going[i])    
                i -= 1
            i+=1

        
        if waiting and (going_weight + waiting[0][0]) <= weight:
            truck = waiting.pop(0)
            going.append(truck)
            going_weight += truck[0]


    answer = time
    return answer

n, w, l = map(int, input().split())
truck_weights = list(map(int, input().split()))
print(solution(int(w), int(l), truck_weights))