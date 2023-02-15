# 유닛 이동시키기_2194_BFS

from collections import deque
import sys
input=sys.stdin.readline

n,m,a,b,k=map(int,input().split())
graph=[[0]*m for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(k):
  x,y=map(int,input().split())
  graph[x-1][y-1]=-1

s_x,s_y=map(int,input().split())
e_x,e_y=map(int,input().split())

def check(nx,ny):
  if nx<0 or nx+a-1>=n or ny<0 or ny+b-1>=m:
    return False
  for i in range(a):
    for j in range(b):
      if graph[nx+i][ny+j]==-1:
          return False
  return True

def bfs():
  q=deque([(s_x-1,s_y-1)])
  while q:
    x,y=q.popleft()
    if x==e_x-1 and y==e_y-1:
      print(graph[x][y])
      return
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if check(nx,ny) and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        q.append((nx,ny))
  print(-1)

bfs()