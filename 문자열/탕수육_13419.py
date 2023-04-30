# 탕수육_13419_문자열

for _ in range(int(input())):
  s=input()
  if len(s)%2==0:
    print(s[0::2])
    print(s[1::2])
  else:
    print(s[0::2],s[1::2],sep='')
    print(s[1::2],s[0::2],sep='')
