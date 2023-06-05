from sys import stdin

N, S = map(int, stdin.readline().split())
sequence = list(map(int, stdin.readline().split()))

answer = float("inf")
tmp_sum = sequence[0]
end = 0
for start in range(N):
    while tmp_sum < S and end < len(sequence) - 1:
        end += 1
        tmp_sum += sequence[end]
        
    if tmp_sum >= S:
        answer = min(answer, end - start + 1)
        tmp_sum -= sequence[start]
    else:
        break
if answer == float("inf"):
    print(0)
else:
    print(answer)