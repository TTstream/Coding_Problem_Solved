# 내 선물을 받아줘 2_15886_DFS

n=int(input())
arr=list(input())
visited=[0]*n

def dfs(x):
  if visited[x]: return
  visited[x]=1

  if arr[x]=='E':
    dfs(x+1)
  else:
    dfs(x-1)

cnt=0
for i in range(n):
  if visited[i]==0 and arr[i]=='E':
    dfs(i)
    cnt+=1

print(cnt)