# 1번부터 문제의 상태가...?_23027_문자열

s=input()

if 'A' in s:
  for i in 'BCDF':
    s=s.replace(i,'A')
elif 'B' in s:
  for i in 'CDF':
    s=s.replace(i,'B')
elif 'C' in s:
  for i in 'DF':
    s=s.replace(i,'C')
else:
  s='A'*len(s)

print(s)
