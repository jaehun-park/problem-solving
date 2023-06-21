from sys import stdin

g, s = map(int, stdin.readline().split())
W, S = stdin.readline().strip(), stdin.readline().strip()

word, window = [0] * 58, [0] * 58
cnt = 0

for ch in W:
    word[ord(ch) - 65] += 1

for i, ch in enumerate(S):
    window[ord(ch) - 65] += 1

    if i >= g - 1:
        cnt += 1 if window == word else 0
        window[ord(S[i - g + 1]) - 65] -= 1

print(cnt)
