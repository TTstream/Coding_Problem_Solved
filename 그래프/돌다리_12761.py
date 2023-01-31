# 돌다리_12761_BFS | 같은유형 # 숨바꼭질_1697_BFS

import sys
input=sys.stdin.readline
from collections import deque

stone=[0]*100001
a,b,n,m=map(int,input().split())

def bfs(x):
  q=deque([x])
  while q:
    x=q.popleft()
    if x==m:
      print(stone[x])
      return
    for dx in (x-1,x+1,x+a,x-a,x+b,x-b,x*a,x*b):
      if 0<=dx<100001 and stone[dx]==0:
        stone[dx]=stone[x]+1
        q.append(dx)

bfs(n)