def convert(n, k):
    result = ''
    num = n
    while num > 0:
        result = str(num % k) + result
        num //= k
    return result


def is_prime_num(k):
    major = [2, 3, 5, 7]
    
    if k in major: return True
    if k % 2 == 0 or k < 2: return False
    
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def solution(n, k):
    n_list = convert(n , k).split('0')
    answer = 0
    
    for num in n_list:
        if num == "": continue
        if is_prime_num(int(num)):
             answer += 1
    return answer

