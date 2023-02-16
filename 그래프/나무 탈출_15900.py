# 나무 탈출_15900_DFS
# 참고사이트 https://wookcode.tistory.com/152

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0,0]+[-1]*(n-1)

for _ in range(n-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v):
  for i in graph[v]:
    if visited[i]==-1:
      visited[i]=visited[v]+1
      dfs(i)

dfs(1)

result=0
for i in range(2,n+1): # 리프노드일 경우
  if len(graph[i])==1:
    result+=visited[i]

print("Yes" if result%2==1 else "No") #홀수면 승