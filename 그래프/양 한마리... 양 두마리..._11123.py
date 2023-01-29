# 양 한마리... 양 두마리..._11123_BFS

from collections import deque
import sys
input=sys.stdin.readline

def bfs(i,j):
  q=deque([(i,j)])
  graph[i][j]=1
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w:
        if graph[nx][ny]=='#':
          graph[nx][ny]=1
          q.append((nx,ny))
          
t=int(input())
d=[(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(t):
  h,w=map(int,input().split())
  graph=[list(map(str,input().strip())) for _ in range(h)]

  result=0
  for i in range(h):
    for j in range(w):
      if graph[i][j]=='#':
        bfs(i,j)
        result+=1
  print(result)