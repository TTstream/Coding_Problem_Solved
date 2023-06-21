# 준살 프로그래밍 대회_7513_문자열

for cnt in range(int(input())):

  li=[input() for _ in range(int(input()))]
  
  print(f"Scenario #{cnt+1}:")
  for _ in range(int(input())):
    password=list(map(int,input().split()))
    answer=''.join([li[i] for i in password[1:]])
    print(answer)
  print()
