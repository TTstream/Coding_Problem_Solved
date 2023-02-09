# 무한부스터_17391_BFS

from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

def bfs():
  q=deque([(0,0)])
  while q:
    x,y=q.popleft()
    for i in range(1,graph[x][y]+1):
      for dx,dy in ((0,i),(i,0)):
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
          visited[nx][ny]=visited[x][y]+1
          if nx==n-1 and ny==m-1:
            print(visited[nx][ny])
            return
          q.append((nx,ny))
      
bfs()