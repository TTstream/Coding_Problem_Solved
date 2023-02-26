# IBM 빼기 1_6321_문자열

n=int(input())
for i in range(n):
  s=input()
  result=''
  for j in s:
    v=ord(j)+1
    if v==91:v=65
    result+=chr(v)

  print(f"String #{i+1}")
  print(result)
  print()