# 사칙연산_13420_문자열

for _ in range(int(input())):
  a,b=map(str,input().split('='))
  print("correct" if eval(a)==int(b) else "wrong answer")