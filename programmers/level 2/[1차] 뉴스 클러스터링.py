def make_set(input_str):
    result = [input_str[i:i+2].lower()
              for i in range(len(input_str)-1)
              if input_str[i:i+2].isalpha()]
    return result


def solution(str1, str2):
    arr1 = make_set(str1)
    arr2 = make_set(str2)
    
    intersection = 0
    for em in arr1:
        if em in arr2:
            arr2.remove(em)
            intersection += 1
    
    union = len(arr1) + len(arr2)
    
    if union == 0:
        answer = 65536
    else:
        answer = int((intersection / union) * 65536)
    return answer