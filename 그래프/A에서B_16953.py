# A -> B_16953_BFS

import sys
input=sys.stdin.readline
from collections import deque

a,b=map(int,input().split())

def bfs():
  q=deque([(a,0)])
  while q:
    x,cnt=q.popleft()
    if x==b:
      print(cnt+1)
      return
    for i in ((x*2),int(str(x)+"1")):
      if 0<=i<=b:
        q.append((i,cnt+1))
  print(-1)
  return 

bfs()