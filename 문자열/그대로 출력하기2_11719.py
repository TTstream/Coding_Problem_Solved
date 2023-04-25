# 그대로 출력하기2_11719_문자열
# EOF = EOF란 파일의 끝을 의미하며, 갑자기 파일의 끝이 올 것을 예상하지 못할 때 발생하는 오류
# ctrl + z 엔터를 이용해 예외상황 만들기
while True:
  try:
    print(input())
  except EOFError:
    break