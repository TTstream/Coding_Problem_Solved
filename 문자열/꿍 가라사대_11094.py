# 꿍 가라사대_11094_문자열

for _ in range(int(input())):
  s=input()
  x=s.find("Simon says")
  if "Simon says" in s:
    print(s[x+10:])

