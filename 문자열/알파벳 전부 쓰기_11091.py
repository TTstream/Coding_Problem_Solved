# 알파벳 전부 쓰기_11091_문자열

for _ in range(int(input())):
  s=input().replace(" ","").lower()
  alphabet=[0]*26
  result=''
  for i in s:
    if 'a'<=i<='z':
      alphabet[ord(i)-97]+=1
  for j in range(len(alphabet)):
    if alphabet[j]==0:
      result+=chr(j+97)
  print("pangram" if result=='' else "missing "+result)
