# 명령 프롬프트_1032_문자열

n=int(input())
word=list(input())
word_len=len(word)

for _ in range(n-1):
  word2=list(input())
  for i in range(word_len):
    if word[i]!=word2[i]:
      word[i]='?'

print(''.join(word))
