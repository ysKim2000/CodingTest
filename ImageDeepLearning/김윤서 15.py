# 2750번

import sys
input = sys.stdin.readline


def solution_15(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    for i in nums:
        print(i)


N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))   
solution_15(nums)
