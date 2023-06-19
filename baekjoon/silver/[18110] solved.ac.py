from sys import stdin


def my_round(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)


N = int(stdin.readline())
options = sorted([int(stdin.readline()) for _ in range(N)])
critical_point = my_round(N * 0.15)
seleted_option = options[critical_point:-critical_point] if critical_point != 0 else options

print(my_round(sum(seleted_option) / len(seleted_option)) if len(seleted_option) != 0 else 0)
