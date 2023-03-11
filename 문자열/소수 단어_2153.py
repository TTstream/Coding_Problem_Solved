# 소수 단어_2153_문자열

s=input()
result=0
for i in s:
  if 'a'<=i<='z':
    result+=ord(i)-96
  elif 'A'<=i<='Z':
    result+=ord(i)-38

def is_prime(x):
  for i in range(2,x):
    if x%i==0:
      return False
  return True

if is_prime(result):
  print("It is a prime word.")
else:
  print("It is not a prime word.")