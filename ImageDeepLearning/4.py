import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열
res = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        res[i][j] = res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + arr[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(res[x2][y2] - res[x2][y1 - 1] - res[x1 - 1][y2] + res[x1 - 1][y1 - 1]) # 첫 부분은 중복되므로 더함