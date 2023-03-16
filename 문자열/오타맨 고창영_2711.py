# 오타맨 고창영_2711_문자열

for _ in range(int(input())):
  x,y=input().split()
  x=int(x)
  print(f'{y[:x-1]}{y[x:]}')