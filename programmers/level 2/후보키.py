from itertools import combinations 

def is_candidate_key(relation, key):
    attr_set = set()
    for row in relation:
        attr_set.add(tuple([row[i] for i in range(len(relation[0])) if i in key]))
    return True if len(relation) == len(attr_set) else False


def key_combinations(col_size):
    result = []
    for i in range(col_size, 0, -1):
        result += list(combinations(range(col_size), i))
    return result


def solution(relation):
    answer = 0
    keys = key_combinations(len(relation[0]))
    while keys:
        tmp = keys.pop()
        if is_candidate_key(relation, tmp):
            answer += 1
            keys = [key for key in keys if set(tmp) & set(key) != set(tmp)]
    return answer