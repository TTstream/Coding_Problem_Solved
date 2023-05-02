# 신용카드 판별_14726_문자열

for _ in range(int(input())):
  s=input()
  cnt=0
  for i in range(len(s)):
    if i%2==0:
      num=int(s[i])*2
      if num>=10:
        num=str(num)
        cnt+=int(num[0])+int(num[1])
      else:
        cnt+=num
    else:
      cnt+=int(s[i])
  print("T" if cnt%10==0 else "F")
