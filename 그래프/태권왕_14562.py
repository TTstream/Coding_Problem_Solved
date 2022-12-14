# 태권왕_14562_BFS
from collections import deque

def bfs(s,t):
  cnt=0
  q=deque()
  q.append([s,t,cnt])
  while q:
    s,t,cnt=q.popleft()
    if s<t:
      q.append([s*2,t+3,cnt+1])
      q.append([s+1,t,cnt+1])
    elif s==t:
      print(cnt)
      break
for _ in range(int(input())):
  s,t=map(int,input().split())
  bfs(s,t)