# 트리의 부모 찾기_11725_DFS

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
graph=[[] for _ in range(n+1)]
parent=[0]*(n+1)

for _ in range(n-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v):
  for i in graph[v]:
    if parent[i]==0:
      parent[i]=v
      dfs(i)

dfs(1)
for i in range(2,n+1):
  print(parent[i])