# 해밍 거리_3449_문자열

for _ in range(int(input())):
  a=input()
  b=input()
  print(f"Hamming distance is {sum([1 for i in range(len(a)) if a[i]!=b[i]])}.")