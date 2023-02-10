# 현명한 나이트_18404_BFS

from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[-1]*n for _ in range(n)]
d=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

k_x,k_y=map(int,input().split())

result=[]
for _ in range(m):
  x,y=map(int,input().split())
  graph[x-1][y-1]='E'
  result.append((x-1,y-1))

def bfs():
  q=deque([(k_x-1,k_y-1)])
  graph[k_x-1][k_y-1]=0
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny]==-1 or graph[nx][ny]=='E':
          graph[nx][ny]=graph[x][y]+1
          q.append((nx,ny))

bfs()
for i,j in result:
  print(graph[i][j],end=' ')