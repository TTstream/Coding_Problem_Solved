# 헌내기는 친구가 필요해_21736_BFS

from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
d=[(1,0),(-1,0),(0,1),(0,-1)]

graph=[list(input()) for _ in range(n)]
visited=[[0]*(m) for _ in range(n)]

def bfs(i,j):
  global cnt
  q=deque([(i,j)])
  visited[i][j]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+d[i][0]
      ny=y+d[i][1]
      if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
        visited[nx][ny]=1
        if graph[nx][ny]=='O':
          q.append((nx,ny))
        if graph[nx][ny]=='P':
          cnt+=1
          q.append((nx,ny))
        
cnt=0
for i in range(n):
  for j in range(m):
    if graph[i][j]=='I':
      bfs(i,j)
    
print(cnt if cnt else "TT")