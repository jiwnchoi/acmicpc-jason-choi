n, k = map(int, input().split())
people = [i for i in range(1,n+1)]
position = 0
print("<", end="")
while(len(people) > 1):
    position = (position+k-1)%(len(people))
    print("%d, "%people[position], end="")
    del(people[position])

print("%d>"%people[0],  end="")