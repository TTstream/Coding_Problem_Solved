# 눈덩이 굴리기_21735_DFS

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[0]+list(map(int,input().split()))

def dfs(index,size,time):
  global ans
  if time>m:
    return
  if time<=m:
    ans=max(ans,size) 
  if index<=n-1:
    dfs(index+1,size+arr[index+1],time+1)
  if index<=n-2:
    dfs(index+2,size//2+arr[index+2],time+1)
ans=-1
dfs(0,1,0)
print(ans)