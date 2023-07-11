from sys import stdin

N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))

best_score = sum(cards[::2])
my_turn, your_turn = best_score, best_score
for i in range(N - 2, -1, -2):
    my_turn += cards[i + 1] - cards[i]
    your_turn += cards[i - 1] - cards[i] if i > 0 else 0
    best_score = max(best_score, my_turn, your_turn)
print(best_score)
