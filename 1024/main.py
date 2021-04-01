#1024

n, l = input().split(" ")
n= int(n)
l = int(l)
ans = 0
for i in range(l,101,1):
    if(i % 2 == 0):
        if(n % i) == (i / 2) :
            if (n//i-n%i+1 < 0):
                continue
            else:
                for j in range(n//i-n%i+1,n//i+n%i,1):
                    print(j,end=" ")
                print(n//i+n%i)
                ans = 1
                break
    else:
        if(n%i) == 0:
            if(n//i-i//2 < 0):
                continue
            else:
                for j in range(n//i-i//2,(n//i)+(i//2),1):
                    print(j,end= " ")
                print((n//i)+(i//2))
                ans =1
                break
if(ans == 0):
    print(-1)
