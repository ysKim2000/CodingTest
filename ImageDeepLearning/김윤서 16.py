# 1377번

import sys
input = sys.stdin.readline


def solution_16(nums):
    cnt = 0

    nums = merge_sort(nums)
    for i in range(len(nums)) :
        cnt = max(cnt, nums[i][1] - i + 1)

    print(cnt)

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


N = int(input())
nums = []
for i in range(N):
    nums.append((int(input()), i))
solution_16(nums)
