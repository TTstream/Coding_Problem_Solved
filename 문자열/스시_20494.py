# 스시_20494_문자열

li=[0]*26
for _ in range(int(input())):
  s=input()
  for i in s:
    li[ord(i)-65]+=1
print(sum(li))

