n, m = map(int, input().split())

det = list()
bo = list()


for _ in range(n):
    det.append(input())
for _ in range(m):
    bo.append(input())

jobs = list(set(det) & set(bo))
jobs.sort()
print(len(jobs))
for job in jobs:
    print(job)