# 가장 많은 글자_1371_문자열

import sys

n=sys.stdin.read().replace(' ','').replace('\n','')
result=[0]*26

for i in n:
  result[ord(i)-97]+=1

print(''.join([chr(j+97) for j in range(26) if result[j]==max(result)]))