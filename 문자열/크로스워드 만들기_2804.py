# 크로스워드 만들기_2804_문자열

a,b=input().split()
for i in a:
  if i in b:
    x=a.index(i)
    y=b.index(i)
    break

arr=''
for i in range(len(b)):
  if i==y:
    print(a)
  else:
    print('.'*x+b[i]+'.'*(len(a)-x-1))
