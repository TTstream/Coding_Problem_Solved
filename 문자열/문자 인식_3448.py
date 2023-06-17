# 문자 인식_3448_문자열

for _ in range(int(input())):
  tmp=[0,0]
  while True:
    s=input()
    if s=='':
      break
    else:
      tmp[0]+=len(s)
      tmp[1]+=len(s)-s.count('#')
  hap=round(tmp[1]*100/tmp[0],1)   
  
  if hap % 1 == 0:
    print("Efficiency ratio is %d%%." % int(hap))
  else:
    print("Efficiency ratio is %.1f%%." % hap)
