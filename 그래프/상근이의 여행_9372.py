# 상근이의 여행_9372_DFS
import sys

for _ in range(int(sys.stdin.readline())):
  n,m=map(int,sys.stdin.readline().split()) # n=국가의 수 m=비행기의 종류
  graph=[[] for _ in range(n+1)]

  for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
  
  visited=[0]*(n+1)

  def dfs(v,cnt):
    visited[v]=1
    for i in graph[v]:
      if visited[i]==0:
        cnt=dfs(i,cnt+1)
    return cnt

  print(dfs(1,0))