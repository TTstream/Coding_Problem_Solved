# 효율적인 해킹_1325_bfs_pypy3제출

from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
  x,y=map(int,input().split())
  graph[y].append(x)

def bfs(num):
  q=deque([num])
  cnt=1
  visited=[0]*(N+1)
  visited[num]=1
  while q:
    num=q.popleft()
    for i in graph[num]:
      if visited[i]==0:
        visited[i]=1
        cnt+=1
        q.append(i)
  
  return cnt

max_cnt=0
result=[]
for i in range(1,N+1):
  tmp=bfs(i)
  if max_cnt==tmp:
    result.append(i)
  if max_cnt<tmp:
    max_cnt=tmp
    result=[]
    result.append(i)

print(*result)