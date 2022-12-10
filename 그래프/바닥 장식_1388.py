# 바닥 장식_1388_DFS
def dfs(x, y):
    if graph[x][y] == '|':
        graph[x][y] = '.'
        for i in [1,-1]:
          X=x+i
          if 0<=X<N and graph[X][y]=='|':
           dfs(X,y)
    if graph[x][y] == '-':
        graph[x][y] = '.'
        for i in [1, -1]:
         Y=y+i
         if 0<=Y<M and graph[x][Y]=='-':
          dfs(x, Y)

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
  for j in range(M):
      if graph[i][j] == '|' or graph[i][j] == '-':
        dfs(i, j)
        result += 1
print(result)