from sys import stdin
from itertools import product

N = int(stdin.readline())
cases = product(['0', '1', '2'], repeat=N)
print(len([case for case in cases if case[0] != '0' and int(''.join(case)) % 3 == 0]))