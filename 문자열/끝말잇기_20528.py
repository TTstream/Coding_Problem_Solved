# 끝말잇기_20528_문자열

n=int(input())
s=input().split()
answer=set()

for i in range(n):
  answer.add(s[i][0])
print("1" if len(answer)==1 else "0")
