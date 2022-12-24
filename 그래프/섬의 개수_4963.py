#섬의 개수_4963_DFS,BFS

# DFS
'''
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
  dx=[1,-1,0,0,1,-1,1,-1]
  dy=[0,0,1,-1,1,-1,-1,1]
  graph[x][y]=0

  for i in range(8):
    X,Y=x+dx[i],y+dy[i]
    if 0<=X<h and 0<=Y<w:
      if graph[X][Y]==1:
        dfs(X,Y)

while True:
  w,h=map(int,input().split())
  if w==0 and h==0: break
  graph=[list(map(int,input().split())) for _ in range(h)]
  # print(*graph,sep='\n')

  count=0
  for i in range(h):
    for j in range(w):
      if graph[i][j]==1:
        dfs(i,j)
        count+=1
  print(count)
'''

# BFS
'''
from collections import deque

def bfs(i,j):
  d=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
  q=deque([(i,j)])
  graph[i][j]=0
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w:
        if graph[nx][ny]==1:
          graph[nx][ny]=0
          q.append((nx,ny))

while True:
  w,h=map(int,input().split())
  if w==0 and h==0: break
  graph=[list(map(int,input().split())) for _ in range(h)]
  
  result=0
  for i in range(h):
    for j in range(w):
      if graph[i][j]==1:
        bfs(i,j)
        result+=1
  
  print(result)
'''
