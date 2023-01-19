# 케빈 베이컨의 6단계 법칙_1389_BFS(플로이드워셜로도 풀수있음)

from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(start):
  q=deque([start])
  check=[0]*(N+1)
  check[start]=1
  while q:
    start=q.popleft()
    for i in graph[start]:
      if check[i]==0:
        check[i]=check[start]+1
        q.append(i)
  return sum(check)

result=[]
for start in range(1,N+1):
  result.append(bfs(start))
print(result.index(min(result))+1)