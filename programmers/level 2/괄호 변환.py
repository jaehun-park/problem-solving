def seperate(s):
    cnt = 0
    is_right = True
    idx = 0
    for i, ch in enumerate(s):
        if ch == '(': cnt += 1
        else: cnt -= 1
        
        if cnt < 0: is_right = False
        if cnt == 0: 
            idx = i
            break
    return s[:idx+1], s[idx+1:], is_right


def reverse(s):
    result = ''
    for ch in s:
        if ch == '(': 
            result += ')'
        else: 
            result += '('
            
    return result


def transpose(s):
    if s == "": return ""

    u, v, u_is_right = seperate(s)
    
    if u_is_right:
        return u + transpose(v)
    else:
        u = reverse(u[1:-1])
        return '(' + transpose(v) + ')' + u
    
    
def solution(p):
    answer = transpose(p)
    return answer