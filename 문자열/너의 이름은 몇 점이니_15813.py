# 너의 이름은 몇 점이니?_15813_문자열

n=int(input())
s=input()
answer=0
for i in s:
  answer+=ord(i)-64
print(answer)
