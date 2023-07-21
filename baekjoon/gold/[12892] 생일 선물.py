from sys import stdin

N, D = map(int, stdin.readline().split())
gifts = sorted([list(map(int, stdin.readline().split())) for _ in range(N)])
max_happiness = 0
happiness = 0
e = 0
for s in range(N):
    while e < N:
        if gifts[e][0] - gifts[s][0] >= D:
            break
        else:
            happiness += gifts[e][1]
        e += 1
    max_happiness = max(max_happiness, happiness)
    happiness -= gifts[s][1]

print(max_happiness)
