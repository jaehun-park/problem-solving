from sys import stdin

N = int(stdin.readline())
graph = [int(stdin.readline()) - 1 for _ in range(N)]

answer = []

for i in range(N):
    temp = i
    for _ in range(N):
        if graph[temp] == i:
            answer.append(i)
            break
        temp = graph[temp]

print(len(answer))
for num in answer:
    print(num + 1)
