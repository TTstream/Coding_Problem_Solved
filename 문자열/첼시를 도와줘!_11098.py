# 첼시를 도와줘!_11098_문자열

for _ in range(int(input())):
  li={}
  for _ in range(int(input())):
    a,b=input().split()
    li[int(a)]=b
  print(li[max(li)])
