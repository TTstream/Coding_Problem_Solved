# 파일 완전 삭제_9243_문자열

n=int(input())
a,b=list(input()),list(input())
for _ in range(n):
  for i in range(len(a)):
    if a[i]=='0':
      a[i]='1'
    else:
      a[i]='0'
print("Deletion succeeded" if a==b else "Deletion failed")