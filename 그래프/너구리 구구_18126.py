# 너구리 구구_18126
# 참고사이트 https://velog.io/@daeungdaeung/%EB%B0%B1%EC%A4%80-18126-%EB%84%88%EA%B5%AC%EB%A6%AC%EA%B5%AC%EA%B5%AC

from collections import deque

n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
  x,y,z=map(int,input().split())
  graph[x].append([y,z])
  graph[y].append([x,z])

visited=[0]*(n+1)

maxresult=0
def bfs(v,l):
  global maxresult
  visited[v]=1
  q=deque()
  q.append([v,l])

  while q:
    v,l=q.popleft()
    
    for i,j in graph[v]:
      if visited[i]==0:
        visited[i]=1
        q.append([i,j+l])

    if l>maxresult:
      maxresult=l

bfs(1,0)
print(maxresult)