# 음식물 피하기_1743_BFS

from collections import deque
import sys
input=sys.stdin.readline

N,M,K=map(int,input().split()) #N:세로 M:가로 K:음식을 쓰레기 개수
arr=[[0]*M for _ in range(N)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(K):
  x,y=map(int,input().split())
  arr[x-1][y-1]=1

def bfs(i,j):
  global result
  max_dish=0
  q=deque([(i,j)])
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx,ny=x+d[i][0],y+d[i][1]
      if 0<=nx<N and 0<=ny<M:
        if arr[nx][ny]==1:
          arr[nx][ny]=0
          q.append((nx,ny))
          max_dish+=1
  
  if result<max_dish:
    result=max_dish

result=float("-inf")
for i in range(N):
  for j in range(M):
    if arr[i][j]==1:
      bfs(i,j)

print(result)