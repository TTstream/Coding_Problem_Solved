# 그래프 탐색 2_14218_BFS

from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split()) 
graph=[[] for _ in range(n+1)]

for _ in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs():
  visited=[-1]*(n+1)
  q=deque([1])
  visited[1]=0
  while q:
    v=q.popleft() 
    for i in graph[v]:
      if visited[i]==-1:
        visited[i]=visited[v]+1
        q.append(i)

  print(*[visited[i] for i in range(1,n+1)])
  return

q=int(input().strip())
for _ in range(q):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

  bfs()