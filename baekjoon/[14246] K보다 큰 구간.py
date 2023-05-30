from sys import stdin

N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
K = int(stdin.readline())

tmp_sum, start_num = numbers[0], numbers[0]
start, end = 0, 0
answer = 0

while start < N and end < N:
    while tmp_sum <= K and end < N - 1:
        end += 1
        tmp_sum += numbers[end]
    
    if tmp_sum <= K:
        break
    
    answer += N - end
    
    start += 1
    tmp_sum -= start_num
    start_num = numbers[start]
    
print(answer)