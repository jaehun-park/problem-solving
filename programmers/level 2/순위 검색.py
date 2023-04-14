import collections, bisect

def solution(info_list, query_list):
    answer = [0] * len(query_list)
    info_dict = collections.defaultdict(list)
    
    for info in info_list:
        info = info.split(' ')
        info_dict[' '.join(info[:4]) + ' -'].append(int(info[4]))
    
    for key in info_dict:
        info_dict[key].sort()
    
    keys = list(info_dict.keys())
    
    for i, query in enumerate(query_list):
        query = [q for q in query.split(' ') if q != 'and']
        
        for key in [key for key in keys if all(cond in key for cond in query[:4])]:
            answer[i] += len(info_dict[key]) - bisect.bisect_left(info_dict[key], int(query[4]))

    return answer