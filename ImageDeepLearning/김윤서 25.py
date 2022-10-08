from sys import stdin
input = stdin.readline


def dfs(idx, number):
    if number == 4:
        print(1)
        exit()
    for i in friend[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False


global visited, friend
N, M = map(int, input().split())
friend = [[] for _ in range(N)]
visited = [False] * N


for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
print(0)

