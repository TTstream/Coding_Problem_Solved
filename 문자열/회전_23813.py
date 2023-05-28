# 회전_23813_문자열

n=input()
answer=0
for _ in range(len(n)):
  answer+=int(n)
  n=n[1:]+n[0]
print(answer)
