# Quiz: https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        name = cloth[0]
        kind = cloth[1]
        if kind not in clothes_dict:
            clothes_dict[kind] = 1
        else:
            clothes_dict[kind] += 1
    answer = 1
    for v in clothes_dict.values():
        answer *= (v + 1)
    return answer - 1