# 1427번
# 선택 정렬

import sys
input = sys.stdin.readline


def solution_17(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    for i in range(len(arr)):
        print(arr[i],end="")

arr = list(input())
solution_17(arr)