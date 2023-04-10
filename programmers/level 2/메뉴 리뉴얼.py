from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    candidates_list = [defaultdict(int) for i in range(len(course))]
    answer = []
    for order in orders:
        for i, n in enumerate(course):
            for combination in combinations(order, n):
                candidates_list[i][''.join(sorted(combination))] += 1

    for candidate_dict in candidates_list:
        candidates = sorted(candidate_dict.items(), key=lambda x: x[1], reverse=True)
        if candidates and candidates[0][1] >= 2:
            answer.append(candidates[0][0])
            max_order = candidates[0][1]
            for item in candidates[1:]:
                if item[1] == max_order:
                    answer.append(item[0])
    answer.sort()
    return answer