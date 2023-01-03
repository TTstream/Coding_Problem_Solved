# 텔레포트 정거장_18232_bfs

from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
s,e=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)

for _ in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(v):
  visited[v]=0
  q=deque([v])
  while q:
    v=q.popleft()
    d=[v+1,v-1]
    if graph[v]:
      d+=graph[v]
    for i in d:
      if 1<=i<=n and visited[i]==-1:
        q.append(i)
        visited[i]=visited[v]+1
      if i==e:
        return visited[i]

cnt=bfs(s)
print(cnt)