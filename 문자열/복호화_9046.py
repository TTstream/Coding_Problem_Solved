# 복호화_9046_문자열

for _ in range(int(input())):
  s=input().replace(" ","")
  alphabet=[0]*26
  result=''
  for i in s:
    alphabet[ord(i)-97]+=1
  print("?" if alphabet.count(max(alphabet))>1 else chr(97+alphabet.index(max(alphabet))))