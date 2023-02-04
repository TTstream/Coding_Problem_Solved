# 현수막_14716_BFS

from collections import deque
import sys
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(m)]

d=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

def bfs(i,j):
  q=deque([(i,j)])
  graph[i][j]=0
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<m and 0<=ny<n:
        if graph[nx][ny]==1:
          graph[nx][ny]=0
          q.append((nx,ny))

result=0
for i in range(m):
  for j in range(n):
    if graph[i][j]==1:
      bfs(i,j)
      result+=1
print(result)