# 미로 탐색_2178_BFS

from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
  q=deque([(0,0)])
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny]==1:
          graph[nx][ny]=graph[x][y]+1
          q.append((nx,ny))

bfs()
graph[0][0]=1
print(graph[n-1][m-1])