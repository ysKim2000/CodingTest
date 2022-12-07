# 18352번: 특정 거리의 도시 찾기
from collections import deque
import sys
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
q=deque([])
q.append(x)
dist=[-1]*(n+1)
dist[x]=0
while q:
    now=q.popleft()
    for i in graph[now]:
        if dist[i]==-1:
            q.append(i)
            dist[i]=dist[now]+1
if not k in dist:
    print(-1)
for i in range(len(dist)):
    if dist[i]==k:
        print(i)