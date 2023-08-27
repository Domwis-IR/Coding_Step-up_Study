def solution(nums):
    n = len(nums)
    uniq = list(set(nums))
    if len(uniq) < n/2:
        return len(uniq)
    else:
        return int(n/2)
