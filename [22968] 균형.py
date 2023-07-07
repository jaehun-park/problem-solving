from sys import stdin

N, M = map(int, stdin.readline().split())
num_to_name = [stdin.readline().strip() for _ in range(N)]
q = [stdin.readline().strip() for _ in range(M)]
name_to_num = dict()
for i, name in enumerate(num_to_name):
    name_to_num[name] = i + 1
for s in q:
    if s.isalpha():
        print(name_to_num[s])
    else:
        print(num_to_name[int(s) - 1])
