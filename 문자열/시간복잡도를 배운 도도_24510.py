# 시간복잡도를 배운 도도_24510_문자열

max_s=0
for _ in range(int(input())):
  s=input()
  cnt=s.count('for')+s.count('while')
  if max_s<cnt:
    max_s=cnt
print(max_s)
