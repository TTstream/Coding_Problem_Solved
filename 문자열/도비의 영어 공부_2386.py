# 도비의 영어 공부_2386_문자열

while True:
  s=input()
  if s[0]=='#': break
  print(f"{s[0]} {s.count(s[0])+s.count(chr(ord(s[0])-32))-1}")