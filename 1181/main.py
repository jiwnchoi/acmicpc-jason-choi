n = int(input())
words = list()
for _ in range(n):
    words.append(input())

words = list(set(words))
words.sort()
words = sorted(words, key=lambda x : len(x))

for i in words:
    print(i)