# 8진수_2998_문자열
# 내 풀이

n=input()
arr=['000','001','010','011','100','101','110','111']
while len(n)%3!=0:
  n='0'+n

for i in range(len(n)//3):
  result=n[i*3:(i*3)+3]
  if result in arr:
    print(arr.index(result),end='')


# 다른풀이 2진수를 10진수로 변환 후 10진수를 8진수로 변환

x=oct(int(input(),2))
print(x[2:])
