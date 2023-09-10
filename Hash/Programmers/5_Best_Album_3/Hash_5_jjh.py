def solution(genres, plays):
    answer = []
    c_dict = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if c_dict.get(genre):
            temp = c_dict.get(genre)
            temp.append([play,i])
            c_dict[genre] = temp
        else:
            c_dict[genre] = [[play, i]]
    n_dict = dict()
    for key, value in c_dict.items():
        s_dict = sorted(value, reverse =True)
        temp_sum = sum([i[0] for i in value])
        n_dict[temp_sum] = s_dict
    print (n_dict)
        
    while n_dict:
        temp_m = max(n_dict.keys())
        value = n_dict.get(temp_m)
            
        if len(value) == 1:
            answer.append(value[0][1])
            n_dict.pop(temp_m)
            continue
        elif value[0][0] == value[1][0]:
            answer.append(value[1][1])
            answer.append(value[0][1])
            n_dict.pop(temp_m)
            continue
        for i in range(2):
            answer.append(value[i][1])
        n_dict.pop(temp_m)

    
    return answer
