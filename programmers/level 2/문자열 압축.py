def compression(s, unit):
    s = [s[i:i+unit] for i in range(0, len(s), unit)] + ['']
    result, cnt = [], 1
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            if cnt > 1: result.append(str(cnt))
            result.append(s[i])
            cnt = 1
        else:
            cnt += 1
    return ''.join(result)


def solution(s):
    return min([len(compression(s, unit)) for unit in range(1, int(len(s)/2)+2)])