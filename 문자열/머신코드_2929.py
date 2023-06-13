# 머신코드_2929_문자열

import re
s=input()

ss=re.split('(?=[A-Z])',s)

cnt=0
for i in range(1,len(ss)-1):
  a=len(ss[i])%4
  if a!=0: cnt+=(4-a)
print(cnt)

