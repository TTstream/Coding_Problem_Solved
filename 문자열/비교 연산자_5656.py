# 비교 연산자_5656_문자열

cnt=1
while True:
  num1,oper,num2=input().strip().split()
  re=False
  num1,num2=int(num1),int(num2)
  if oper=='E':
    break
  if oper=='!=':
    re= num1!=num2
  elif oper=='<':
    re= num1<num2
  elif oper=='>':
    re= num1>num2
  elif oper=='<=':
    re= num1<=num2
  elif oper=='>=':
    re= num1>=num2
  elif oper=='==':
    re= num1==num2
  
  print(f"Case {cnt}: {str(re).lower()}")
  cnt+=1