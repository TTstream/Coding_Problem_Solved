# 점프왕 쩰리_16174_BFS

from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

def bfs():
  q=deque([(0,0)])
  visited[0][0]=1
  while q:
    x,y=q.popleft()
    if x==n-1 and y==n-1:
      print("HaruHaru")
      return
    for dx,dy in ((graph[x][y],0),(0,graph[x][y])):
      nx,ny=x+dx,y+dy
      if 0<=nx<n and 0<=ny<n:
        if visited[nx][ny]==0:
          visited[nx][ny]=1
          q.append((nx,ny))
  print("Hing")
  return

bfs()