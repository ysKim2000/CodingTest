# 11399번
# 삽입 정렬

import sys
input = sys.stdin.readline

def solution_18(N, arr):
    tmp = 0
    res = []
    arr = insertion_sort(arr)
    for i in range(N):
        tmp += arr[i]
        res.append(tmp)

    print(sum(res))

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr


N = int(input())
arr = list(map(int, input().split()))
solution_18(N, arr)
