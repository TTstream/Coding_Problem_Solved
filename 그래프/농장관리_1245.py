# 농장관리_1245_BFS

import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
visited=[[0]*m for _ in range(n)]

def bfs(i,j):
  global trigger
  q=deque([(i,j)])
  visited[i][j]=1
  while q:
   x,y=q.popleft()
   for dx,dy in d:
     nx,ny=x+dx,y+dy
     if 0<=nx<n and 0<=ny<m:
       if graph[i][j]<graph[nx][ny]:
         trigger=False
       if graph[i][j]==graph[nx][ny] and visited[nx][ny]==0:
         visited[nx][ny]=1
         q.append((nx,ny))
        
result=0
for i in range(n):
  for j in range(m):
    if graph[i][j]!=0 and visited[i][j]==0:
      trigger=True
      bfs(i,j)
      
      if trigger:
        result+=1
print(result)