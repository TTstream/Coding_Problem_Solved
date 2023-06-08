# 누울 자리를 찾아라_1652_문자열

n=int(input())
room=[input() for _ in range(n)]
answer=[0,0]

for i in range(n):
  r=c=0
  for j in range(n):
    if room[i][j]=='.':
      r+=1
    else:
      r=0
    if r==2:
      answer[0]+=1
    
    if room[j][i]=='.':
      c+=1
    else:
      c=0
    if c==2:
      answer[1]+=1

print(*answer)
