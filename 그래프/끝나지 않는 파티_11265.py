# 끝나지 않는 파티_11265_플로이드 와샬 or 다익스트라 알고리즘_PyPy3제출

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
party=[list(map(int,input().split())) for _ in range(n)]

#거쳐가는 노드
for k in range(n):
  #출발 노드
  for i in range(n):
    #도착 노드
    for j in range(n):
      if party[i][k]+party[k][j]<party[i][j]:
        party[i][j]=party[i][k]+party[k][j]

for _ in range(m):
  #a:서비스를 요청한 손님이 위치한 파티장의 번호
  #b:다음 파티가 열리는 파티장의 번호
  #c:다음 파티가 열리는데 걸리는 시간
  a,b,c=map(int,input().split())
  if party[a-1][b-1]<=c:
    print('Enjoy other party')
  else:
    print('Stay here')