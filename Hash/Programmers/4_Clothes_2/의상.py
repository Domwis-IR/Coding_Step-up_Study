def solution(clothes):
    answer = 1
    hash = {}
    for i in clothes:
        if i[1] in hash:
            hash[i[1]].append(i[0])
        else:
            hash[i[1]] = [i[0]]
    
    for i in hash.keys():
        answer = answer * (len(hash[i])+1)
    return answer-1
            