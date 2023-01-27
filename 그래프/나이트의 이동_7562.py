# 나이트의 이동_7562_BFS

import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
d=[(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]
  
for _ in range(n):
  I=int(input())
  chess=[[0]*I for _ in range(I)]

  now_x,now_y=map(int,input().split())
  arrival_x,arrival_y=map(int,input().split())

  def bfs(i,j):
    q=deque([(i,j)])
    while q:
      x,y=q.popleft()
      if x==arrival_x and y==arrival_y:
        print(chess[x][y])
        return
      for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<I and 0<=ny<I:
          if chess[nx][ny]==0:
            chess[nx][ny]=chess[x][y]+1
            q.append((nx,ny))

  bfs(now_x,now_y)