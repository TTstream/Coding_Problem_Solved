# 모르고리즘 회장님 추천 받습니다_20124_문자열

li,lis={},[]
for _ in range(int(input())):
  a,b=input().split()
  li[a]=int(b)

li_max=max(li.values())
for i in li.keys():
  if li[i]==li_max:
    lis.append(i)

lis.sort()
print(lis[0])
