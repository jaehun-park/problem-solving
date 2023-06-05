from sys import stdin

N = int(stdin.readline())
features = list(map(int, stdin.readline().split()))
features.sort(key=lambda x: abs(x))

answer = [0, 0]
best_feature = float("inf")

for i in range(len(features) - 1):
    if abs(features[i] + features[i+1]) < best_feature:
        best_feature = abs(features[i] + features[i+1])
        answer[0], answer[1] = features[i], features[i+1]

answer.sort()
print(answer[0], answer[1])