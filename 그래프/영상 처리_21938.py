# 영상 처리_21938_BFS

import sys
input=sys.stdin.readline
from collections import deque

N,M=map(int,input().split())

graphic=[]
for i in range(N):
  graph=list(map(int,input().split()))
  temp=[]
  for j in range(M):
    temp.append(int(sum(graph[3*j:3*(j+1)])/3))
  graphic.append(temp)

T=int(input())

visited=[[0]*M for _ in range(N)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j):
  q=deque([(i,j)])
  visited[i][j]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx,ny=x+d[i][0],y+d[i][1]
      if 0<=nx<N and 0<=ny<M:
        if visited[nx][ny]==0 and graphic[nx][ny]>=T:
          q.append((nx,ny))
          visited[nx][ny]=1

cnt=0
for i in range(N):
  for j in range(M):
    if graphic[i][j]>=T and visited[i][j]==0:
      bfs(i,j)
      cnt+=1

print(cnt)