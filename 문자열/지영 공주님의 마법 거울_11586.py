# 지영 공주님의 마법 거울_11586_문자열

n=int(input())
arr=[input() for _ in range(n)]
k=int(input())

if k==1:
  print(*arr,sep='\n')
elif k==2:
  print(*[i[::-1] for i in arr],sep='\n')
else:
  print(*arr[::-1],sep='\n')