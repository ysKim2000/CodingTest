# 11004번
import random
random.seed(42)
from sys import stdin

def solution_19(K, arr):
    arr = quick_sort(arr, K)
    print(arr)

def quick_sort(arr, K):
    pivot = arr[random.randint(0, len(arr) - 1)]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    _len = [len(lesser_arr), len(equal_arr)]
    if K <= _len[0]:
        return quick_sort(lesser_arr, K)
    elif K <= sum(_len):
        return pivot
    else:
        return quick_sort(greater_arr, K - sum(_len))


N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
solution_19(K, A)