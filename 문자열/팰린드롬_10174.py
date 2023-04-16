# 팰린드롬_10174_문자열

for _ in range(int(input())):
  s=input().lower()
  print("Yes" if s==s[::-1] else "No")