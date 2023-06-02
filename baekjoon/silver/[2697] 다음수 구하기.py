from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    number = list(stdin.readline().strip())
    if number == sorted(number, reverse=True):
        print("BIGGEST")
        continue
    
    i = len(number) - 2
    while number[i] >= number[i+1]:
        i -= 1
        
    j = len(number) - 1
    while number[i] >= number[j]:
        j -= 1
    
    number[i], number[j] = number[j], number[i]
    next_number = number[:i+1] + sorted(number[i+1:])
    print(''.join(next_number))