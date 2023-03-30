# 패리티_4597_문자열

while True:
  x=input()
  if x=='#':
    break
  cnt_1=x.count('1')
  s=''
  s+=x[:-1]
  if x[-1]=='e':
    if cnt_1%2==0:
      s+='0'
    else:
      s+='1'
  else:
    if cnt_1%2==0:
      s+='1' 
    else:
      s+='0'
  print(s)