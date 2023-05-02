# 인생 점수_15351_문자열

for _ in range(int(input())):
  s=input().replace(" ","")
  cnt=0
  for i in s:
    cnt+=ord(i)-64
  print("PERFECT LIFE" if cnt==100 else cnt)
