# 안전 영역_2468_BFS

from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

max_h=max(map(max,graph))

def bfs(i,j,rain):
  q=deque([(i,j)])
  visited[i][j]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      dx,dy=x+d[i][0],y+d[i][1]
      if 0<=dx<n and 0<=dy<n:
        if graph[dx][dy]>rain and visited[dx][dy]==0:
          visited[dx][dy]=1
          q.append((dx,dy))

max_safe=0
for rain in range(0,max_h):
  visited=[[0]*n for _ in range(n)]
  safe=0
  for i in range(n):
    for j in range(n):
      if graph[i][j]>rain and visited[i][j]==0:
        bfs(i,j,rain)
        safe+=1
  max_safe=max(max_safe,safe)
print(max_safe)