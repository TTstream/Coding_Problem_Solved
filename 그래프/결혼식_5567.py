# 결혼식_5567_bfs

from collections import deque

n=int(input())
m=int(input())
friend=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  friend[a].append(b)
  friend[b].append(a)

def bfs(v):
  visited[v]=1
  q=deque([v])
  while q:
    v=q.popleft()
    for i in friend[v]:
      if visited[v]<3 and visited[i]==0:
        visited[i]=visited[v]+1
        q.append(i)

bfs(1)
print(len(visited)-visited.count(0)-1)