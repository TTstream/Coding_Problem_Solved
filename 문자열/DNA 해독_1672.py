# DNA 해독_1672_문자열

n=int(input())
s=list(input())
d_s={"AG":"C","AC":"A","AT":"G","GC":"T","GT":"A","CT":"G"}

a,b='',s.pop()
for _ in range(n-1):
  a=s.pop()
  if a==b:
    continue

  if a+b in d_s:
    b=d_s[a+b]
  else:
    b=d_s[b+a]

print(b)