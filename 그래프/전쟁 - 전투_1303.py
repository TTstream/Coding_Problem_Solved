# 전쟁 - 전투_1303_BFS

import sys
input=sys.stdin.readline
from collections import deque

M,N=map(int,input().split())

graph=[list(input().strip()) for _ in range(N)]
d=[(0,1),(0,-1),(1,0),(-1,0)]

def bfs(i,j,color):
  cnt=1
  q=deque([(i,j)])
  graph[i][j]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx,ny=x+d[i][0],y+d[i][1]
      if 0<=nx<N and 0<=ny<M:
        if graph[nx][ny]==color:
          cnt+=1
          q.append((nx,ny))
          graph[nx][ny]=1
  
  return cnt
  
white=blue=0
for i in range(N):
  for j in range(M):
    if graph[i][j]=='W':
      white+=bfs(i,j,'W')**2
    if graph[i][j]=='B':
      blue+=bfs(i,j,'B')**2

print(white,blue)