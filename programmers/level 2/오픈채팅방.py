def solution(record):
    nicknames = {log.split()[1]:log.split()[2] for log in record if not log.startswith('Leave')}
    answer = []
    for log in record:
        log = log.split()
        if log[0] == 'Enter': answer.append(f'{nicknames[log[1]]}님이 들어왔습니다.')
        elif log[0] == 'Leave': answer.append(f'{nicknames[log[1]]}님이 나갔습니다.')
    
    return answer