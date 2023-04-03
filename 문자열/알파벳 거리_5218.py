# 알파벳 거리_5218_문자열
'''
for _ in range(int(input())):
  x,y=input().split()
  result=[]
  for i in range(len(x)):
    o_x,o_y=ord(x[i]),ord(y[i])
    if o_y>=o_x:
      result.append(o_y-o_x)
    else:
      result.append((o_y+26)-o_x)
  print('Distances:',*result)
'''