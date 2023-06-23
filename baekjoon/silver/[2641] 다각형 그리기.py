from sys import stdin

TABLE = {"1": "3", "2": "4", "3": "1", "4": "2"}
N = int(stdin.readline())
std_seq = stdin.readline().strip()
std_rvs_seq = std_seq[::-1].translate(str.maketrans("".join(list(TABLE.keys())), "".join(list(TABLE.values()))))
M = int(stdin.readline())
seq_list = [(stdin.readline().strip() + " ") * 2 for _ in range(M)]
answers = [seq for seq in seq_list if std_seq in seq or std_rvs_seq in seq]

print(len(answers))
for ans in answers:
    print(ans[: N * 2])
