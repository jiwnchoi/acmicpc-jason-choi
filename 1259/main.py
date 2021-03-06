def check(w):
    for i in range(0,(len(w)//2)):
        if(w[i] != w[len(w)-i-1]):
            return 0
    return 1


while True:

    w = input()
    
    if( w == "0"):
        break
    if(check(w) == 1):
        print("yes")
    else:
        print("no")
