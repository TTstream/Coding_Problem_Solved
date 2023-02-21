# 모음의 개수_1264_문자열

while True:
  s=input()
  if s=='#':
    break
  cnt=0
  for i in s:
    if i in 'aeiouAEIOU':
      cnt+=1
  print(cnt)