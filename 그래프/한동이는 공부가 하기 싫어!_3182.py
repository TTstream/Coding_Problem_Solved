# 한동이는 공부가 하기 싫어!_3182_DFS

n=int(input())
graph=[[] for _ in range(n+1)]
max_visited=[0]*(n+1)

for i in range(1,n+1):
  v=int(input())
  graph[i].append(v)

def dfs(v,cnt):
  visited[v]=1
  n=graph[v][0]
  if visited[n]==0:
    cnt=dfs(n,cnt+1)
  return cnt

for i in range(1,n+1):
  visited=[0]*(n+1)
  max_visited[i]=dfs(i,1)

print(max_visited.index(max(max_visited)))