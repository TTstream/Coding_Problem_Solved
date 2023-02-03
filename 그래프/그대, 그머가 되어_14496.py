# 그대, 그머가 되어_14496_BFS

from collections import deque

a,b=map(int,input().split())
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)

for _ in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs():
  q=deque([a])
  visited[a]=0
  while q:
    v=q.popleft()
    if v==b:
      return print(visited[v])
    for i in graph[v]:
      if visited[i]==-1:
        visited[i]=visited[v]+1
        q.append(i)

  print(-1)
  return

bfs()