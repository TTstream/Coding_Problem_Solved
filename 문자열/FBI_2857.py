# FBI_2857_문자열

li=[]
for i in range(5):
  n=input()
  if "FBI" in n:
    li.append(i+1)

if li:
  print(*li)
else:
  print("HE GOT AWAY!")