# 노드사이의 거리_1240_BFS
# https://dongdongfather.tistory.com/69 -> defaultdict 사용법
# graph=defaultdict(list) 중복허용O | graph=defaultdict(set) 중복허용X

'''
from collections import defaultdict, deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=defaultdict(list)

for _ in range(n-1):
  a,b,dis=map(int,input().split())
  graph[a].append((b,dis))
  graph[b].append((a,dis))

def bfs(a,b):
  q=deque([a])
  visited=[-1]*(n+1)
  visited[a]=0
  while q:
    x=q.popleft()
    if x==b:
      print(visited[b])
      return
    for node,dis in graph[x]:
      if visited[node]==-1:
        visited[node]=visited[x]+dis
        q.append(node)

for _ in range(m):
  a,b=map(int,input().split())
  bfs(a,b)
'''