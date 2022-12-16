# 죽음의 게임_17204_BFS
'''
from collections import deque

n,k=map(int,input().split())
graph=[int(input()) for _ in range(n)]

def bfs(v):
  q=deque([v])
  cnt=0
  for _ in range(n):
    x=q.popleft()
    cnt+=1
    if graph[x]==k:
      return cnt
    q.append(graph[x])
  return -1
  
print(bfs(0))
'''

# 다른풀이
'''
from collections import deque

def bfs():
  q=deque([0])
  while q:
    x=q.popleft()
    n=lis[x]
    if check[n]==0:
      q.append(n)
      check[n]=check[x]+1
      if n==k:
        return

n,k=map(int,input().split())
lis=[int(input()) for _ in range(n)]
check=[0]*(n)
bfs()
print(check[k] if check[k] else -1)
'''