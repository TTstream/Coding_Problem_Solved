# 유진수_1356_문자열

n=input()
answer="NO"
for i in range(len(n)-1):
  left=right=1
  for j in range(i+1):
    left*=n[j]
  for k in range(i+1,len(n)):
    right*=n[k]
  if left==right:
    answer="YES"
    break
print(answer)

