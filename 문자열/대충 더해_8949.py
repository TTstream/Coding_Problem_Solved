# 대충 더해_8949_문자열

a,b=input().split()
la,lb=len(a),len(b)
result=''
if la>lb:
  b='0'*(la-lb)+b
else:
  a='0'*(lb-la)+a
for i in range(len(a)):
  result+=str(int(a[i])+int(b[i]))
print(result)