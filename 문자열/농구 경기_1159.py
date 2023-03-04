# 농구 경기_1159_문자열

arr={}
n=int(input())
for _ in range(n):
  a=input()[0]
  if a not in arr:
    arr[a]=1
  else:
    arr[a]+=1

result=[]
for i,j in arr.items():
  if j>=5:
    result.append(i)

if result: print(''.join(sorted(result)))
else: print("PREDAJA")