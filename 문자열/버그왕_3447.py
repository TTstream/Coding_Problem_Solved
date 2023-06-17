# 버그왕_3447_문자열

import sys 

s=sys.stdin.readlines()
for i in s:
  while True:
    answer=i.replace("BUG","")
    if "BUG" in answer: i=answer
    else:
      print(answer,end='')
      break
