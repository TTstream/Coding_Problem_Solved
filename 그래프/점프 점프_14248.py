# 점프 점프_14248_BFS

from collections import deque

n=int(input())
graph=list(map(int,input().split()))
s=int(input())-1
visited=[0]*n

def bfs(s):
  q=deque([s])
  visited[s]=1
  while q:
    y=q.popleft()
    for dy in [graph[y],-graph[y]]:
      Y=dy+y
      if 0<=Y<n and visited[Y]==0:
        visited[Y]=1
        q.append(Y)

bfs(s)
print(visited.count(1))