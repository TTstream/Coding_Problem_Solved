# 양_3184

from collections import deque
def bfs(i,j):
  global o,v
  to,tv=0,0
  q=deque([[i,j]])
  if graph[i][j] == "o": to += 1
  elif graph[i][j] == "v": tv += 1
  while q:
    x,y=q.popleft()
    for i in range(4):
      X,Y=x+dx[i],y+dy[i]
      if 0<=X<R and 0<=Y<C and graph[X][Y]!="#" and visited[X][Y]==0:
        if graph[X][Y]=="o":
          to+=1
        if graph[X][Y]=="v":
          tv+=1
        visited[X][Y]=1
        q.append([X,Y])

  if to>tv:
    v-=tv
  else:
    o-=to
    
R,C=map(int,input().split())
# '.':빈필드 '#':울타리 'o':양 'v':늑대
graph=[list(input()) for _ in range(R)] 
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visited=[[0]*(C) for _ in range(R)]

o,v=0,0
for i in range(R):
  for j in range(C):
    if graph[i][j]=="o": o+=1
    if graph[i][j]=="v": v+=1
  
for i in range(R):
  for j in range(C):
    if graph[i][j]=="v" or graph[i][j]=="o" and visited[i][j]==0:
      visited[i][j]=1
      bfs(i,j)

print(o,v)