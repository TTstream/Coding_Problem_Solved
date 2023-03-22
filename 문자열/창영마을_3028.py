# 창영마을_3028_문자열

arr=[1,0,0]
s=input()
for i in s:
  if i=='A':
    arr[0],arr[1]=arr[1],arr[0]
  elif i=='B':
    arr[1],arr[2]=arr[2],arr[1]
  elif i=='C':
    arr[0],arr[2]=arr[2],arr[0]
print(arr.index(1)+1)