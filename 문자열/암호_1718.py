# 암호_1718_문자열
# https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj1718/ 참고사이트

# 내 풀이
arr='abcdefghijklmnopqrstuvwxyz'

a,b=input(),input()
z=[arr.index(i) for i in b]

for i in range(len(a)):
  if a[i]==' ':print(end=' ')
  else:
    w=arr.index(a[i])-z[i%len(b)]
    print(arr[w-1],end='')

# 다른 사람 풀이
a,b=input(),input()
answer=''

for i in range(len(a)):
  if a[i]==' ': answer+=' '
  else: answer+=chr((ord(a[i])-ord(b[i%len(b)])-1)%26+ord('a'))
print(answer)