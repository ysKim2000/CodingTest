# 17298번
# 오큰수

import sys
from collections import deque
input = sys.stdin.readline

def solution_12(N, arr):
    stack = []
    result = [-1 for _ in range(N)]

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    for i in result:
        print(i, end=" ")

def my_solution_12(N, arr):
    arr = deque(arr)
    result = []
    while arr:
        current = arr.popleft()
        exist = False

        for x in arr:
            if current < x:
                result.append(x)
                exist = True
                break
    
        if exist == False:
            result.append(-1)
    for i in result:
        print(i, end=" ")
        
        
N = int(input())
arr = list(map(int, input().split()))
solution_12(N, arr)
