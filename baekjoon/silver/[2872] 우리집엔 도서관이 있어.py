from sys import stdin

N = int(stdin.readline())
books = [int(stdin.readline()) for _ in range(N)]

cnt = 0
for i in range(N, 0, -1):
    if books[i-1] < i + cnt:
        cnt += 1

print(cnt)