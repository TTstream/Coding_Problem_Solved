# 연결 요소의 개수_11724_DFS

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split()) # n:정점의 개수 m:간선의 개수
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v):
  for i in graph[v]:
    if visited[i]==0:
      visited[i]=1
      dfs(i)

result=0
for i in range(1,n+1):
  if visited[i]==0:
    dfs(i)
    result+=1
print(result)