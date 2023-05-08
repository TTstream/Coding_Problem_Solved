# 클레어와 팰린드롬_17502_문자열

n=int(input())
s=list(input())

for i in range(len(s)//2):
  if s[i]!='?' and s[-i-1]=='?':
    s[-i-1]=s[i]
  elif s[i]=='?' and s[-i-1]!='?':
    s[i]=s[-i-1]
  elif (s[i],s[-i-1])==('?','?'):
    s[i]=s[-i-1]='a'
if s[n//2]=='?':
  s[n//2]='a'

print(''.join(s))
