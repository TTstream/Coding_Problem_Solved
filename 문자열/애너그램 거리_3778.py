# 애너그램 거리_3778_문자열

import sys
input=sys.stdin.readline
for _ in range(int(input())):
  a1=[0]*26
  a2=[0]*26
  s1=input().strip()
  s2=input().strip()
  for i in range(len(s1)):
    a1[ord(s1[i])-97]+=1
  for i in range(len(s2)):
    a2[ord(s2[i])-97]+=1
  cnt=0
  for i in range(26):
    cnt+=abs(a1[i]-a2[i])
  print(f"Case #{_+1}: {cnt}")