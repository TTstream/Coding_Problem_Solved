# 자석 체인_17201_문자열

n=int(input())
s=input()
answer="Yes"
for i in range(1,n):
  if s[0:2]!=s[i*2:i*2+2]:
    answer="No"
    break
print(answer)
