# 촌수계산_2644_DFS,BFS
# DFS로 풀음
'''
n=int(input())
a,b=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(int(input())):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(a):
  for i in graph[a]:
    if visited[i]==0:
      visited[i]=visited[a]+1
      dfs(i)

dfs(a)
print(visited[b] if visited[b] else -1)
'''
# BFS로 풀음
'''
from collections import deque

n=int(input())
a,b=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(int(input())):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(a):
  q=deque()
  q.append(a)
  while q:
    a=q.popleft()
    for i in graph[a]:
      if visited[i]==0:
        visited[i]=visited[a]+1
        q.append(i)

bfs(a)
print(visited[b] if visited[b] else -1)
'''