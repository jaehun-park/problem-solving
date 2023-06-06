from sys import stdin
import itertools

N, M = map(int, stdin.readline().split())
cases = itertools.permutations(stdin.readline().split(), M)
cases = [list(map(int, case)) for case in cases]
cases = sorted(cases) + [[]]

for i in range(len(cases) - 1):
    if cases[i] != cases[i + 1]:
        print(' '.join(map(str, cases[i])))