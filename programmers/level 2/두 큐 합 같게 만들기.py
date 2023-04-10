def solution(queue1, queue2):
    diff = sum(queue1) - sum(queue2)
    answer, i, j = 0, 0, 0
    max_iter = len(queue1) + len(queue2) + max(len(queue1), len(queue2)) - 1
    
    while diff != 0 and answer <= max_iter:
        if diff > 0:
            diff -= 2 * queue1[i]
            queue2.append(queue1[i])
            i += 1
        else:
            diff += 2 * queue2[j]
            queue1.append(queue2[j])
            j += 1
        answer += 1
    
    return answer if not diff else -1