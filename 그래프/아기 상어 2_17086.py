# 아기 상어 2_17086_BFS

from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,-1,1]

q=deque()
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      q.append((i,j))

def bfs():
  while q:
    x,y=q.popleft()
    for i in range(8):
      nx,ny=x+dx[i],y+dy[i]
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        q.append((nx,ny))

bfs()
print(max(map(max,graph))-1)
