# 11286번
# 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

def solution_14(N):
    heap = []
    arr = []
    
    for _ in range(N):
        x = int(input())
        arr.append(x)
        numbers = int(arr.pop(0))

        if numbers != 0:
            heapq.heappush(heap, (abs(numbers), numbers))
        else:
            if not heap:
                print(0)                            
            else:
                print(heapq.heappop(heap)[1])


N = int(input())
solution_14(N)
