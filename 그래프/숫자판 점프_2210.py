# 숫자판 점프_2210_DFS

def dfs(x,y,number):
  if len(number)==6:
    if number not in result:
      result.append(number)
    return 
  for dx,dy in d:
    nx,ny=x+dx,y+dy
    if 0<=nx<5 and 0<=ny<5:
      dfs(nx,ny,number+graph[nx][ny])

graph=[list(map(str,input().split())) for _ in range(5)]
d=[(-1,0),(1,0),(0,1),(0,-1)]

result=[]
for i in range(5):
  for j in range(5):
    dfs(i,j,graph[i][j])
print(len(result))