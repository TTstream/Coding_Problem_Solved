# 작업_21937_DFS

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
  x,y=map(int,input().split())
  graph[y].append(x)
X=int(input())

def dfs(v):
  global cnt
  for i in graph[v]:
    if not visited[i]:
      visited[i]=1
      cnt+=1
      dfs(i)

cnt=0
dfs(X)
print(cnt)