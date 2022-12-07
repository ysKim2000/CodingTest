n, m = map(int, input().split())
A = [list(map(int, input()))for _ in range(n)]
Q = [(0, 0)]
while Q:
 i, j = Q.pop(0)
 for x, y in (i, j+1), (i+1, j), (i, j-1), (i-1, j):
  if 0 <= x < n and 0 <= y < m and A[x][y] == 1:
   A[x][y] = A[i][j]+1
   Q += [(x, y)]
print(A[-1][-1])