# 점프 점프_11060_BFS

import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
maze=list(map(int,input().split()))
visited=[-1]*(n)

def bfs(v):
  q=deque([v])
  visited[v]=0
  while q:
    v=q.popleft()
    for i in range(1,maze[v]+1,1):
      if i+v<n and visited[i+v]==-1:
        visited[i+v]=visited[v]+1
        q.append(i+v)
      
bfs(0)
print(visited[-1])