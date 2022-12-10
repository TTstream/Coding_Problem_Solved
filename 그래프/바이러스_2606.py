#BFS
from collections import deque

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)
visited=[0]*(n+1)

def bfs(v):
  visited[v]=1
  q=deque()
  q.append(v)
  while q:
    v=q.popleft()
    for i in graph[v]:
      if visited[i]==0:
        q.append(i)
        visited[i]=1

bfs(1)
print(sum(visited)-1)

#DFS
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)
visited=[0]*(n+1)

def dfs(v):
  visited[v]=1
  for i in graph[v]:
    if visited[i]==0:
      dfs(i)

dfs(1)
print(sum(visited)-1)