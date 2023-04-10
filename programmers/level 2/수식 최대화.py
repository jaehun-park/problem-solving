from itertools import permutations
import re

def apply_operator(expression, operator):
    i = 0
    while i < len(expression):
        if expression[i] == operator:
            expression.insert(i-1, str(eval(''.join(expression[i-1:i+2]))))
            del expression[i:i+3]
            i -= 2
        i += 1
       
            
def solution(expression):    
    answer = 0
    cases = permutations(['+', '-', '*'], 3)
    expression = re.split('([^0-9])', expression)
    
    for case in cases:
        tmp = expression[:]
        apply_operator(tmp, case[0])
        apply_operator(tmp, case[1])
        apply_operator(tmp, case[2])
        answer = max(answer, abs(int(tmp[0])))

    return answer