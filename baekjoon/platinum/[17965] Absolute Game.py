N = int(input())
seq_a, seq_b = [sorted(list(map(int, input().split()))) for _ in range(2)]
answer = 0

for i in range(N):
    min_dist = float("inf")
    for j in range(N):
        min_dist = min(min_dist, abs(seq_a[i] - seq_b[j]))
    answer = max(answer, min_dist)

print(answer)
