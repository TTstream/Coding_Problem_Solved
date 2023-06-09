# 암호_1855_문자열

# 다른분 풀이
n=int(input())
s=input()
arr=[]
for i in range(0,len(s),n):
  arr.append(list(s[i:i+n]))

for i in range(len(arr)):
  if i%2!=0:
    ss=list(reversed(arr[i]))
    arr[i]=ss

re=''
for i in range(n):
  for j in range(len(arr)):
    re+=arr[j][i]
    
print(re)

# 내 풀이
n=int(input())
s=input()
r=''
for i in range(len(s)//n):
  if i%2!=0:
    r+=s[i*n:i*n+n][::-1]
  else:
    r+=s[i*n:i*n+n]

print(''.join(r[i+j*n] for i in range(n) for j in range(len(s)//n)))
