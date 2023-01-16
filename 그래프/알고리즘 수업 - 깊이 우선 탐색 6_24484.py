# 알고리즘 수업 - 깊이 우선 탐색 6_24484_DFS

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
d_visited=[-1]*(N+1)
t_visited=[0]*(N+1)

for _ in range(M):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,N+1):
  graph[i].sort(reverse=True)

def dfs(v,depth):
  global cnt
  d_visited[v]=depth
  t_visited[v]=cnt
  for i in graph[v]:
    if d_visited[i]==-1:
      cnt+=1
      dfs(i,depth+1)

cnt=1
dfs(R,0)
result=0
for i in range(1,N+1):
  result+=d_visited[i]*t_visited[i]
print(result)