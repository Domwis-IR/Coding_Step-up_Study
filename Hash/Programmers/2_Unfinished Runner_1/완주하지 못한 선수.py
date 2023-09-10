def solution(participant, completion):
    hash = {}
    for i in participant:
        if i in hash:
            hash[i] +=1
        else:
            hash[i] = 1
            
    for j in completion:
        if hash[j] == 1:
            del hash[j]
        else:
            hash[j] -=1
    answer = list(hash.keys())[0]
    return answer