# 숨바꼭질_1697_BFS

from collections import deque
import sys
input=sys.stdin.readline

N,K=map(int,input().split())
visited=[0]*(100001)

def bfs():
  q=deque([N])
  while q:
    x=q.popleft()
    if x==K:
      print(visited[x])
      break
    for i in (x+1,x-1,x*2):
      if 0<=i<100001 and visited[i]==0:
        visited[i]=visited[x]+1
        q.append(i)

bfs()