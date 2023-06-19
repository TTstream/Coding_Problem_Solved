# 비밀 편지_5426_문자열

for _ in range(int(input())):
  s=input()
  s_len=int(len(s)**(1/2))
  r=''
  for i in range(s_len,-1,-1):
    r+=s[i-1::s_len]
  print(r[:len(s)])
