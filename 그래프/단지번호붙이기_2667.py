# 단지번호붙이기_2667_BFS

from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().strip())) for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j):
  q=deque([(i,j)])
  graph[i][j]=0
  cnt=1
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny]==1:
          graph[nx][ny]=0
          q.append((nx,ny))
          cnt+=1
  return cnt

result=[]
result_count=0
for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      result.append(bfs(i,j))
      result_count+=1

print(result_count)
result.sort()
print(*result,sep='\n')