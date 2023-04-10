# 한다 안한다_5789_문자열
# 마지막으로 고르는 두 숫자로 결정을 내리는 것이므로 중간값 구하기

for _ in range(int(input())):
  s=input()
  cnt=len(s)//2
  print("Do-it" if s[cnt-1]==s[cnt] else "Do-it-Not")
