from sys import stdin

s = stdin.readline().strip()
is_palindrome = [[False for _ in s] for _ in s]

for i in range(len(s)):
    for j in range(i, min(i + 2, len(s))):
        if s[i] == s[j]:
            is_palindrome[i][j] = True

for i in range(len(s) - 1, -1, -1):
    for j in range(i + 2, len(s)):
        if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
            is_palindrome[i][j] = True

dp = [float("inf") for _ in s] + [0]
for end in range(len(s)):
    for start in range(end + 1):
        if is_palindrome[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)
print(dp[-2])
