# 박사 과정_5026_문자열

for _ in range(int(input())):
  s=input()
  if s!="P=NP":
    a,b=map(int,s.split('+'))
    print(a+b)
  else:
    print("skipped")