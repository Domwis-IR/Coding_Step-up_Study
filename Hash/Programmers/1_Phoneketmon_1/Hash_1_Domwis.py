# Quiz: https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    count = len(nums) // 2
    unique_values = {}
    for n in nums:
        if n not in unique_values.keys():
            unique_values[n] = 1
        else:
            unique_values[n] += 1
    if count <= len(unique_values.keys()):
        return count
    else:
        return len(unique_values.keys())

def __main__():
    print(solution([3,1,2,3]))