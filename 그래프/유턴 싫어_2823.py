# 유턴 싫어_2823

from collections import deque

R,C=map(int,input().split())
graph=[list(map(str,input())) for _ in range(R)]
d=[(-1,0),(1,0),(0,-1),(0,1)]
visited=[[0]*C for _ in range(R)]
check=[]

for i in range(R):
  for j in range(C):
    if graph[i][j]==".":
      check.append((i,j))

def bfs():
  q=deque([check[0]])
  while q:
    x,y=q.popleft()
    cnt=0
    for dx,dy in d:
      X,Y=x+dx,y+dy
      if 0<=X<R and 0<=Y<C and graph[X][Y]==".":
          cnt+=1
          if visited[X][Y]==0:
            visited[X][Y]=1
            q.append((X,Y))
    
    if cnt<2:
      return print(1)
  return print(0)

bfs()