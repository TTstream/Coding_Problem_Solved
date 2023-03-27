# 좋은놈 나쁜놈_4447_문자열

for _ in range(int(input())):
  s=input()
  g=s.count('g')+s.count('G')
  b=s.count('b')+s.count('B')
  result=''
  if g>b:
    result='GOOD'
  elif g<b:
    result='A BADDY'
  else:
    result='NEUTRAL'
  print(f'{s} is {result}')