# 알고리즘 수업 - 깊이 우선 탐색 1_24479_DFS

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)

for _ in range(M):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,N+1):
  graph[i].sort()
  
def dfs(v):
  global cnt
  visited[v]=cnt
  for i in graph[v]:
    if visited[i]==0:
      cnt+=1
      dfs(i)
  
cnt=1
dfs(R)
print(*[visited[i] for i in range(1,N+1)],sep='\n')