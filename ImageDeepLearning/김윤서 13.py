# 2164번
# 카드 게임

import sys
from collections import deque 
input = sys.stdin.readline


def solution_13(N):
    queue = deque(i for i in range(1, N+1))
    while len(queue) > 1:
        queue.popleft()
        num = queue.popleft()
        queue.append(num)
    print(queue[0])

N = int(input())
solution_13(N)
