# 팀 이름 정하기_1296_문자열

yeondoo=input()
n=int(input())
max,max_index=0,0
team=sorted([input() for _ in range(n)])
for i in range(n):
  L=yeondoo.count('L')+team[i].count("L")
  O=yeondoo.count('O')+team[i].count("O")
  V=yeondoo.count('V')+team[i].count("V")
  E=yeondoo.count('E')+team[i].count("E")
  answer=((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
  if max<answer:
   max_index=i
   max=answer
print(team[max_index])
