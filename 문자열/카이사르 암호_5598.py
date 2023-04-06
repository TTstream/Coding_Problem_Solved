# 카이사르 암호_5598_문자열

# 한줄로 풀이 print(''.join([chr(ord(i)-3+26) if ord(i)-3<65 else chr(ord(i)-3) for i in s]))

s=input()
word=''
for i in s:
  re=ord(i)-3
  if re<65:
    word+=chr(re+26)
  else:
    word+=chr(re)
print(word)