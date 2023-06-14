# 비밀 이메일_2999_문자열

s=input()
s_len=len(s)
r=1
lis=[]
for i in range(1,s_len+1):
  if s_len%i==0:
    lis.append(i)
lis_len=len(lis)
if lis_len%2==0:
  r=lis[lis_len//2-1]
else:
  r=lis[lis_len//2]
for i in range(r):
  print(s[i::r],end='')
