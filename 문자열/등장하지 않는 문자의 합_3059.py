# 등장하지 않는 문자의 합_3059_문자열
# 전체 알파벳(al) - 입력 값(s) = 남은 문자들(의 아스키코드 값으로 누적)

al={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

for _ in range(int(input())):
  s=set(input())

  result=0
  for i in al-s:
    result+=ord(i)
  print(result)

