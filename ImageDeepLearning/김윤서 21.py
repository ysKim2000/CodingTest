import sys
input = sys.stdin.readline

def solution_21(A):
    merge_sort(A)
    print(cnt)

def merge_sort(arr):
    global cnt

    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []

    l, h = 0, 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
            cnt += len(low_arr) - l

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr  


cnt = 0
N = int(input())
A = list(map(int, input().split()))
solution_21(A)
