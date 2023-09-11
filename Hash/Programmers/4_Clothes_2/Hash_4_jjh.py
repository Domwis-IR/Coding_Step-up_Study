from collections import Counter

def solution(clothes):
    count = 1
    cloth = Counter([i[1] for i in clothes])
    for i in cloth.values():
        count *=(i+1)
        
    return count-1

