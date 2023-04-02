# 가단조와 다장조_5211_문자열

x=input()
s=x.split('|')
ga=da=0
li=''
for i in s:
  li+=i[0]
ga=li.count('A')+li.count('D')+li.count('E')
da=li.count('C')+li.count('F')+li.count('G')

if ga>da or (x[-1] in "ADE" and ga==da):
  print("A-minor")
elif ga<da or (x[-1] in "CFG" and ga==da):
  print("C-major")