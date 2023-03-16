# 비밀편지_2596_문자열

n=int(input())
arr=input()
s=[]
secret=['000000','001111','010011','011100','100110','101001','110101','111010']
for i in range(n):
  s.append(arr[6*i:6*(i+1)])

ans=''
for i in s:
  n_ans=0
  for j in secret:
    cnt=0
    for k in range(6):
      if i[k]==j[k]:
        cnt+=1
    if cnt>=5:
      ans+=chr(secret.index(j)+65)
      break
    else:
      n_ans+=1
  if n_ans==len(secret):
    print(s.index(i)+1)
    quit()
print(ans)