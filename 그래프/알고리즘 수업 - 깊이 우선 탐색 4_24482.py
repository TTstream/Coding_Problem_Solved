# 알고리즘 수업 - 깊이 우선 탐색 4_24482_DFS

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[-1]*(N+1)

for _ in range(M):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,N+1):
  graph[i].sort(reverse=True)

def dfs(v,depth):
  visited[v]=depth
  for i in graph[v]:
    if visited[i]==-1:
      dfs(i,depth+1)

dfs(R,0)
print(*[visited[i] for i in range(1,N+1)],sep='\n')