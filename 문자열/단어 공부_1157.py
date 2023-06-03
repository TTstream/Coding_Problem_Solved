# 단어 공부_1157_문자열

s=input().upper()
s_list=list(set(s))
answer=[]

for i in s_list:
  answer.append(s.count(i))

if answer.count(max(answer))>1:
  print("?")
else:
  print(s_list[answer.index(max(answer))])
