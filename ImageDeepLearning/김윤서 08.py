# 1253번
# 좋다

import sys
input = sys.stdin.readline


def solution_08(N, arr):
    cnt = 0

    for i in range(N):
        tmp = arr[:i] + arr[i+1:]
        start = 0
        end = len(tmp) - 1
        while start != end:
            total = tmp[start] + tmp[end]
            if total == arr[i]:
                cnt += 1
                break
            elif total < arr[i]:
                start += 1
            else:
                end -= 1
    print(cnt)


N = int(input()) 
arr = sorted(list(map(int, input().split()))) 
solution_08(N, arr)