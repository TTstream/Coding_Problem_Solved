# 좋은 자동차 번호판_1871_문자열

for _ in range(int(input())):
  x,y=input().split("-")
  s=0
  for i in range(3):
    s+=(ord(x[i])-65)*26**(2-i)
  print("nice" if abs(s-int(y))<=100 else "not nice")