import sys
from collections import deque
input = sys.stdin.readline


def solution_10(N, L, A):
    q = deque()
    for i in range(N):
        while q and q[-1][0] > A[i]:
            q.pop()
        while q and q[0][1] < i - L + 1:
            q.popleft()
        q.append((A[i],i))
        print(q[0][0], end = ' ')


N, L = map(int, input().split())
A = list(map(int, input().split()))
solution_10(N, L, A)
