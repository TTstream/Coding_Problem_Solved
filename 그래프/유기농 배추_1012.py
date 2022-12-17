# 유기농 배추_1012_DFS

# DFS로 풀음
'''
import sys
sys.setrecursionlimit(10000) # Or sys.setrecursionlimit(10**6)

def dfs(x,y):
  d=[(0,-1),(0,1),(-1,0),(1,0)]
  for dx,dy in d:
    X,Y=x+dx,y+dy
    if 0<=X<m and 0<=Y<n:
      if graph[X][Y]==1:
        graph[X][Y]=-1
        dfs(X,Y)

for _ in range(int(input())):
  m,n,k=map(int,input().split())
  graph=[[0]*(n) for _ in range(m)]
  
  for _ in range(k):
    x,y=map(int,input().split())
    graph[x][y]=1

  result=0
  for i in range(m):
    for j in range(n):
      if graph[i][j]==1:
        dfs(i,j)
        result+=1
  print(result)
'''

# BFS로 풀음
'''
from collections import deque

d=[(0,-1),(0,1),(-1,0),(1,0)]
def bfs(i,j):
  q=deque([(i,j)])
  graph[i][j]=-1
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      X,Y=x+dx,y+dy
      if 0<=X<m and 0<=Y<n:
        if graph[X][Y]==1:
          graph[X][Y]=-1
          q.append((X,Y))
  return

for _ in range(int(input())):
  m,n,k=map(int,input().split())
  graph=[[0]*(n) for _ in range(m)]
  
  for _ in range(k):
    x,y=map(int,input().split())
    graph[x][y]=1

  result=0
  for i in range(m):
    for j in range(n):
      if graph[i][j]==1:
        bfs(i,j)
        result+=1
  print(result)
'''

# DFS로 풀음
'''
import sys
sys.setrecursionlimit(10**6)

for _ in range(int(input())):
  m,n,k=map(int,input().split())
  graph=[[0]*n for _ in range(m)]

  for _ in range(k):
    x,y=map(int,input().split())
    graph[x][y]=1
  
  def dfs(i,j):
    if 0<=i<m and 0<=j<n:
      if graph[i][j]==1:
        graph[i][j]=0
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

  result=0
  for i in range(m):
    for j in range(n):
      if graph[i][j]==1:
        dfs(i,j)
        result+=1
  print(result)
'''