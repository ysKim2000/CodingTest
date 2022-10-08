# 11399번
# 삽입 정렬

import sys
input = sys.stdin.readline

def solution_18(N, arr):
    tmp = 0
    res = []
    arr = merge_sort(arr)
    for i in range(N):
        tmp += arr[i]
        res.append(tmp)

    print(sum(res))


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
arr = list(map(int, input().split()))
solution_18(N, arr)
