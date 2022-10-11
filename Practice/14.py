import sys
import heapq

pq = []
for _ in range(int(input())):    
    N = int(sys.stdin.readline())
    if N: heapq.heappush(pq, (abs(N), N))
    else: print(heapq.heappop(pq)[1] if pq else 0)