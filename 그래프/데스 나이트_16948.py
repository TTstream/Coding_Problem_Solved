# 데스 나이트_16948_BFS

from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[[0]*n for _ in range(n)]
r1,c1,r2,c2=map(int,input().split())

def bfs():
  q=deque([(r1,c1)])
  graph[r1][c1]=1
  while q:
    x,y=q.popleft()
    if graph[r2][c2]:
      print(graph[r2][c2]-1)
      return
    d=[(x-2,y-1),(x-2,y+1),(x,y-2),(x,y+2),(x+2,y-1),(x+2,y+1)]
    for dx,dy in d:
      if 0<=dx<n and 0<=dy<n:
        if graph[dx][dy]==0:
          graph[dx][dy]=graph[x][y]+1
          q.append((dx,dy))
  print(-1)
  return

bfs()