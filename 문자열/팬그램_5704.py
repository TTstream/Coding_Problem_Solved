# 팬그램_5704_문자열

while True:
  s=input().replace(" ","")
  alphabet=[0]*26
  if s=='*':
    break
  for i in s:
    alphabet[ord(i)-97]+=1
  print("Y" if alphabet.count(0)==0 else "N")

# Counter 모듈 사용 풀이
from collections import Counter

while True:
  s=input().replace(" ","")
  if s=='*':
    break
  cnt=Counter(s)
  print("Y" if len(cnt.keys())==26 else "N")
