from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
q = deque()
for i in range(n):
    while q and q[-1][0] > a[i]: q.pop()
    q.append((a[i], i))
    while q[0][1]<=i-l: q.popleft()
    print(q[0][0], end=' ')