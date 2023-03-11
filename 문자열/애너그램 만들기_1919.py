# 애너그램 만들기_1919_문자열

s1=list(input())
s2=list(input())

i=0
while i<len(s1):
  if s1[i] in s2:
    s2.remove(s1[i])
    s1.remove(s1[i])
    i-=1
  i+=1
print(len(s1)+len(s2))
