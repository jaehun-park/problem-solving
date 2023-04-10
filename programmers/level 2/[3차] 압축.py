def solution(msg):
    word_dict = {chr(v + 64):v for v in range(1,27)}
    answer = []
    word = ''
    
    for ch in msg:
        if (word + ch) in word_dict:
            word += ch
            continue
        else:
            answer.append(word_dict[word])
            word_dict[word+ch] = len(word_dict) + 1
            word = ch
    answer.append(word_dict[word])
    
    return answer