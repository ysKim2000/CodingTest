import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열

for i in range(M):
    x1,y1,x2,y2 = map(int, input().split())

