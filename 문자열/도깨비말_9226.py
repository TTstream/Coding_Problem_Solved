# 도깨비말_9226_문자열

while True:
  s=input()
  if s=='#':
    break
  cnt=0
  for _ in range(len(s)):
    if s[0] not in "aeiou":
      s=s[1:]+s[0]
      cnt+=1
    else:
      print(s+"ay")
      break
  if cnt==len(s):
    print(s+"ay")