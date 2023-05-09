# 이상한 나라의 암호_18245_문자열

cnt=1
while True:
  s=input()
  if s=='Was it a cat I saw?':
    break
  cnt+=1
  print(s[0::cnt])
