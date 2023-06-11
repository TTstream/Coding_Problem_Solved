# 동전 게임_2684_문자열

for _ in range(int(input())):
  d = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
  s=input()
  for i in range(38):
    d[s[i:i+3]]+=1
  for j,k in d.items():
    print(k,end=' ')
  print()
