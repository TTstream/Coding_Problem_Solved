# 문자가 몇갤까_7600_문자열

while True:
  s=input().replace(' ', '')
  result=set()
  if s=='#':
    break
  for i in s:
    _i=i.lower()
    if 'a'<=_i<='z':
      result.add(_i)
  print(len(result))