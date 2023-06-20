from sys import stdin

N = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for _ in range(N)]
answers = [0, 0, 0]


def cut(N, m, n):
    num = paper[m][n]
    if N == 1 or all(x == num for line in paper[m : m + N] for x in line[n : n + N]):
        answers[num + 1] += 1
    else:
        N //= 3
        for i in range(3):
            for j in range(3):
                cut(N, m + i * N, n + j * N)


cut(len(paper), 0, 0)
for ans in answers:
    print(ans)
