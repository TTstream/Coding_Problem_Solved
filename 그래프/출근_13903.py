# 출근_13903_BFS

import sys
input=sys.stdin.readline
from collections import deque

r,c=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(r)]

n=int(input())
d=[list(map(int,input().split())) for _ in range(n)]
visited=[[-1]*c for _ in range(r)]

def bfs():
  q=deque()
  for j in range(c):
    if graph[0][j]==1:
      q.append((0,j))
      visited[0][j]=0
      
  while q:
    x,y=q.popleft()
    if x==r-1:
      return visited[x][y]
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<r and 0<=ny<c:
        if graph[nx][ny]==1 and visited[nx][ny]==-1:
          visited[nx][ny]=visited[x][y]+1
          q.append((nx,ny))
  return -1

print(bfs())
