# 점프왕 쩰리(Small)_16173_BFS
# https://bgeun2.tistory.com/45 참고 사이트

from collections import deque

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visit=[[0]*(n) for _ in range(n)]
dx=[1,0] #아래
dy=[0,1] #오른
q=deque()
q.append((0,0))
def bfs():
  while q:
    x,y=q.popleft()

    if arr[x][y]==-1:
      print("HaruHaru")
      return

    j=arr[x][y]
    for i in range(2):
      nx=x+dx[i]*j
      ny=y+dy[i]*j
      if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
        visit[nx][ny]=1
        q.append([nx,ny])

  return print("Hing")

visit[0][0]=1
bfs()