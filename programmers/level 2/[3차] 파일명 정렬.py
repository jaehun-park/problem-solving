import re

def solution(files):
    answer = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    answer = sorted(answer, key=lambda file : re.findall('\D+', file.lower())[0])
    return answer