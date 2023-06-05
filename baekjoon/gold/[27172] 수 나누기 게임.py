from sys import stdin

N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
table = [None for _ in range(1000001)]
for i in range(N):
    table[cards[i]] = 0

for i in range(N):
    for num in range(2 * cards[i], 1000001, cards[i]):
        if table[num] is not None:
            table[cards[i]] += 1
            table[num] -= 1
            
print(' '.join(map(str, [table[card] for card in cards])))          
