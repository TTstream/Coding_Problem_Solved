# 도비의 난독증 테스트_2204_문자열

while True:
  n=int(input())
  s=[]
  if n==0:
    break
  for _ in range(n):
    s.append(input())
  s.sort(key=lambda x: x.lower())
  print(s[0])
