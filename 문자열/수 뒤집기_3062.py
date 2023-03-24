# 수 뒤집기_3062_문자열

for _ in range(int(input())):
  x=input()
  answer=str(int(x)+int(x[::-1]))
  print("YES" if answer==answer[::-1] else "NO")