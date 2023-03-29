# 거울상_4583_문자열

while True:
  s=input()
  if s=='#':
    break

  st=''
  for i in s[::-1]:
    if i not in "bdpqiovwx":
      st="INVALID"
      break
    if i=='b':
      st+='d'
    elif i=='d':
      st+='b'
    elif i=='p':
      st+='q'
    elif i=='q':
      st+='p'
    else:
      st+=i
  print(st)

