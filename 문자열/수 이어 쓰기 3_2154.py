# 수 이어 쓰기 3_2154_문자열

n=int(input())

result=''
for i in range(1,n+1):
  result+=str(i)

print(result.index(str(n))+1)