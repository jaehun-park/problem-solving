from sys import stdin

N, K = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))

result = 1
for n in range(1, N + 1):
    for j in range(len(arr)):
        if arr[j] <= n and (arr[j] - n) % K == 0:
            del arr[j]
            break
        if j + 1 == len(arr):
            result = 0
print(result)
