cnt = [1] * 10
for _ in range(int(input()) - 1):
    cnt = [sum(cnt[i:]) for i in range(10)]
print(sum(cnt) % 10007)