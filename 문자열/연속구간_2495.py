# 연속구간_2495_문자열

for _ in range(3):
  n=input()
  cnt,max_cnt=1,1
  for i in range(1,len(n)):
    if n[i]==n[i-1]: cnt+=1
    else:
      max_cnt=max(max_cnt,cnt)
      cnt=1
  max_cnt=max(max_cnt,cnt)
  print(max_cnt)