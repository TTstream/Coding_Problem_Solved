# 스캐너_3035_문자열

r,c,zr,zc=map(int,input().split())

s=[input() for _ in range(r)]
for i in range(r):
  li=''
  for j in range(c):
    li+=s[i][j]*zc
  for k in range(zr):
    print(li)