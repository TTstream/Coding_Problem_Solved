# 맥주 마시면서 걸어가기_9205_BFS

import sys
input=sys.stdin.readline
from collections import deque

def bfs():
  q=deque([home])
  while q:
    x,y=q.popleft()
    if abs(festival[0]-x)+abs(festival[1]-y)<=1000:
      print("happy")
      return
    for i in range(n):
      if visited[i]==0:
        con_x,con_y=con[i]
        if abs(con_x-x)+abs(con_y-y)<=1000:
          q.append((con_x,con_y))
          visited[i]=1

  print("sad")
  return  

for _ in range(int(input().strip())):
  n=int(input())
  home=list(map(int,input().split()))
  con=[list(map(int,input().split())) for _ in range(n)]
  festival=list(map(int,input().split()))
  visited=[0]*n

  bfs()