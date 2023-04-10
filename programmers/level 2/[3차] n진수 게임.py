STR_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def convert(num, base) :
    result = ''
    tmp = num
    while tmp:
        result = STR_LIST[tmp % base] + result
        tmp = tmp // base
    if not result:
        result = '0'
    return result


def solution(n, t, m, p):
    answer, num, converted_str = '', 0, ''
    
    while len(converted_str) < t * m:
        converted_str += convert(num, n)
        num += 1
    
    answer = converted_str[p-1::m][:t]
    return answer