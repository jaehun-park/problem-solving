import re

waves = [input() for _ in range(int(input()))]
p = re.compile('(100+1+|01)+')

for wave in waves:
    print("YES") if p.fullmatch(wave) else print("NO")