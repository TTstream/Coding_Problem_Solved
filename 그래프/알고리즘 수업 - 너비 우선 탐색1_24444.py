# 알고리즘 수업 - 너비 우선 탐색1_24444_BFS

from collections import deque
import sys
input=sys.stdin.readline

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)

for _ in range(M):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,N+1):
  graph[i].sort()

def bfs(v):
  cnt=1
  q=deque([v])
  visited[v]=1
  while q:
    v=q.popleft()
    for i in graph[v]:
      if visited[i]==0:
        cnt+=1
        visited[i]=cnt
        q.append(i)

bfs(R)  
print(*[visited[i] for i in range(1,N+1)],sep='\n')