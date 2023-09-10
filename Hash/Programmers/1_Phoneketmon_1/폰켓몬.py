import numpy as np
def solution(nums):
    srt = np.unique(nums)
    return min(len(srt), len(nums)//2)