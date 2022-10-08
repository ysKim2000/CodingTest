# 1427번
# 선택 정렬

import sys
input = sys.stdin.readline


def solution_17(arr):
    # for i in range(len(arr) - 1):
    #     min_idx = i
    #     for j in range(i + 1, len(arr)):
    #         if arr[j] > arr[min_idx]:
    #             min_idx = j
    #     arr[i], arr[min_idx] = arr[min_idx], arr[i]
    merge_sort(arr)
    
    for i in range(len(arr)):
        print(arr[i],end="")


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] > high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


arr = list(map(str, sys.stdin.readline().rstrip()))
solution_17(arr)