# 17298번
# 오큰수

import sys
input = sys.stdin.readline

def solution_12(n, arr):
    stack = []
    answer = [-1 for _ in range(n)]

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            answer[stack.pop()] = arr[i]
        stack.append(i)
    print(*answer)
        
N = int(input())
arr = list(map(int, input().split()))
solution_12(N, arr)
