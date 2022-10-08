# 1377번

import sys
input = sys.stdin.readline


def solution_16(nums):
    cnt = 0

    nums = sorted(nums)
    for i in range(len(nums)) :
        cnt = max(cnt, nums[i][1] - i + 1)

    print(cnt)


N = int(input())
nums = []
for i in range(N):
    nums.append((int(input()), i))
solution_16(nums)
