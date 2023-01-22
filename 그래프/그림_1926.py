# 그림_1926_BFS

from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j):
  now_max=1
  q=deque([(i,j)])
  graph[i][j]=0
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny]==1:
          graph[nx][ny]=0
          q.append((nx,ny))
          now_max+=1
  return now_max

picture_count=picture_max=0
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      picture_max=max(picture_max,bfs(i,j))
      picture_count+=1

print(picture_count)
print(picture_max)