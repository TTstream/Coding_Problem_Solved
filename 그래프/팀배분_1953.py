# 팀배분_1953_BFS

from collections import deque

n=int(input())
hate=[[]]
team=[[],[]]

for _ in range(n):
  a=list(map(int,input().split()))
  hate.append(a[1:])

def bfs(v):
  q=deque([v])
  t_number=0
  visited[v]=True
  while q:
    for i in q:
      team[t_number].append(i)
    for _ in range(len(q)):
      v=q.popleft()
      for nv in hate[v]:
        if not visited[nv]:
          visited[nv]=True
          q.append(nv)
    t_number=not t_number

visited=[False]*(n+1)
for i in range(1,n+1):
  if not visited[i]:
    bfs(i)

for i in range(2):
  print(len(team[i]))
  print(*sorted(team[i]))