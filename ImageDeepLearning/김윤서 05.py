'''
1 2 3 1 2
M = 3
3, 12, 12, 123, 231, 312, 12312
1, 2, 4
'''

import sys
N, M = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
arr = [0 for _ in range(M)]

s = 0
cnt = 0

for i in range(N):
    s += A[i]
    res = s % M
    if res == 0:
        cnt += 1

    arr[res] += 1

for i in range(M):
    cnt += arr[i] * (arr[i] - 1) // 2

print(cnt)