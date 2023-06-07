# 수열의 변화_1551_문자열

n,k=map(int,input().split())
s=list(map(int,input().split(',')))
for _ in range(k):
  t=[s[i+1]-s[i] for i in range(len(s)-1)]
  s=t
print(*s,sep=',')
