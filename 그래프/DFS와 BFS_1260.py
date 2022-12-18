# DFS와 BFS_1260

from collections import deque

n,m,v=map(int,input().split()) #n:정점의 개수 m:간선의 개수 v:정점의 번호
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,n+1):
  graph[i].sort()

def dfs(v):
  visited[v]=1
  print(v,end=' ')
  for i in graph[v]:
    if visited[i]==0:
      dfs(i)

def bfs(v):
  visited[v]=0
  q=deque()
  q.append(v)
  while q:
    v=q.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if visited[i]==1:
        visited[i]=0
        q.append(i)

dfs(v)
print()
bfs(v)

