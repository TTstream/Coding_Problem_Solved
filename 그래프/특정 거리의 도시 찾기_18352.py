# 특정 거리의 도시 찾기_18352_BFS

import sys
input=sys.stdin.readline
from collections import deque

n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)

def bfs(v):
  visited[v]=0
  q=deque([v])
  while q:
    v=q.popleft()
    for i in graph[v]:
      if visited[i]==-1:
        visited[i]=visited[v]+1
        q.append(i)
        
bfs(x)
result=False
for i in range(1,n+1):
  if visited[i]==k:
    print(i)
    result=True

if not result:
  print(-1)