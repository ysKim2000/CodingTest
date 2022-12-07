# 2251번: 물의 양 구하기
from collections import deque
import sys
read = sys.stdin.readline

capacity = list(map(int, read().split()))
visited = set()
q = deque([[0, 0, capacity[2]]])
while q:
    curr = q.popleft()
    for i, water in enumerate(curr):
        if water == 0:
            continue
        for j in ((i+1)%3, (i+2)%3):
            water_in_the_target = curr[j]
            water_to_move = min(curr[i], capacity[j] - water_in_the_target)
            nxt = curr[:]
            nxt[i] = nxt[i] - water_to_move
            nxt[j] = nxt[j] + water_to_move
            if tuple(nxt) not in visited:
                q.append(nxt)
                visited.add(tuple(nxt))

print(*sorted([c for a, b, c in visited if a == 0]))