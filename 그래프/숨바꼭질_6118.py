# 숨바꼭질_6118_BFS

from collections import deque

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,n+1):
  graph[i].sort()

def bfs(v):
  q=deque([v])
  visited[v]=1
  while q:
    v=q.popleft()
    for i in graph[v]:
      if visited[i]==0:
        visited[i]=visited[v]+1
        q.append(i)

bfs(1)
print(visited.index(max(visited)),end=' ')
print(max(visited)-1,end=' ')
print(visited.count(max(visited)))