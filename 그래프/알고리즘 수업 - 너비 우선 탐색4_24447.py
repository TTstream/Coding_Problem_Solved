# 알고리즘 수업 - 너비 우선 탐색4_24447_BFS

from collections import deque
import sys
input=sys.stdin.readline

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
d_visited=[-1]*(N+1)
t_visited=[0]*(N+1)

for _ in range(M):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,N+1):
  graph[i].sort()

def bfs(v):
  cnt=1
  d_visited[v]=0
  t_visited[v]=1
  q=deque([v])
  while q:
    v=q.popleft()
    for i in graph[v]:
      if d_visited[i]==-1:
        d_visited[i]=d_visited[v]+1
        cnt+=1
        t_visited[i]=cnt
        q.append(i)

bfs(R)
result=0
for i in range(1,N+1):
  result+=d_visited[i]*t_visited[i]
print(result)