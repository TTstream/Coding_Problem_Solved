# 문어 숫자_1864_문자열

arr={'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1}
while True:
  a=input()
  if a=='#':
    break
  result=0
  for i in range(len(a)):
    result+=arr[a[i]]*8**(len(a)-(i+1))
  print(result)