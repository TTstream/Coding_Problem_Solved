# 침투_13565_BFS

from collections import deque

m,n=map(int,input().split())
arr=[list(map(int,input())) for _ in range(m)]
d=[(-1,0),(1,0),(0,1),(0,-1)]

def bfs(x,y):
  q=deque()
  q.append((x,y))
  arr[x][y]=-1
  while q:
    x,y=q.popleft()
    for i in range(4):
      X,Y=x+d[i][0],y+d[i][1]
      if 0<=X<m and 0<=Y<n:
        if arr[X][Y]==0:
          arr[X][Y]=-1
          q.append((X,Y))

for i in range(n):
  if arr[0][i]==0:
    bfs(0,i)

print("YES" if -1 in arr[-1] else "NO")

