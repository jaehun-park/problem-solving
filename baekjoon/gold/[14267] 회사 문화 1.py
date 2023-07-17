from sys import stdin

n, m = map(int, stdin.readline().split())
parent_nodes = list(map(int, stdin.readline().split()))
child_nodes = [[] for _ in range(n)]
for i, parent in enumerate(parent_nodes[1:]):
    child_nodes[parent - 1].append(i + 1)

dp = [0] * (n)
for i in range(m):
    employee, praise = map(int, stdin.readline().split())
    dp[employee - 1] += praise

stack = [0]
total_praise = 0
while stack:
    temp = stack.pop()
    dp[temp] += dp[parent_nodes[temp] - 1] if temp != 0 else 0
    stack.extend(child_nodes[temp])

print(*dp, sep=" ")
