# 팰린드롬수_1259_문자열

while True:
  s=input()
  if s=='0':
    break
  print("yes"if s==s[::-1] else "no")
