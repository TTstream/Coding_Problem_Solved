# 마술사 이민혁_3023_문자열

r,c=map(int,input().split())
s=[]
for i in range(r):
  a=input()
  s+=[a+a[::-1]]
s+=s[::-1]

a,b=map(int,input().split())

if s[a-1][b-1]=='#':
  s[a-1]=s[a-1][:b-1]+'.'+s[a-1][b:]
else:
  s[a-1]=s[a-1][:b-1]+'#'+s[a-1][b:]

print(*s,sep='\n')
