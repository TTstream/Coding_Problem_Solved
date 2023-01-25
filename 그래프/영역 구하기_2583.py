# 영역 구하기_2583_BFS

import sys
input=sys.stdin.readline
from collections import deque

m,n,k=map(int,input().split()) 
graph=[[0]*n for _ in range(m)]
d=[(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(k):
  x1,y1,x2,y2=map(int,input().split())
  for i in range(y1,y2):
    for j in range(x1,x2):
      graph[i][j]=1

def bfs(i,j):
  q=deque([(i,j)])
  graph[i][j]=1
  cnt=1
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<m and 0<=ny<n:
        if graph[nx][ny]==0:
          graph[nx][ny]=1
          q.append((nx,ny))
          cnt+=1
  return cnt

result=[]
result_count=0
for i in range(m):
  for j in range(n):
    if graph[i][j]==0:
      result.append(bfs(i,j))
      result_count+=1

print(result_count)
result.sort()
print(*result)