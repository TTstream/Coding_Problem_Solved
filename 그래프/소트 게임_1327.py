# 소트 게임_1327_BFS

# 입력값
# 5 3
# 5 4 3 2 1 (54321)
# 출력값
# 34521 52341 54123
# 54321 32541 34125 | 32541 54321 52143 | 14523 52143 54321

from collections import deque

n,k=map(int,input().split())
word=input().split()
sum_word=''.join(word)

visited=set(sum_word)

def bfs():
  global result
  q=deque([(sum_word,0)])
  while q:
    words,cnt=q.popleft()
    list_words=list(words)
    if list_words==sorted(sum_word):
      result=cnt
      return
    for i in range(n-k+1):
      list_new_word=list(words)
      list_result_word=list_new_word[i:i+k]
      list_result_word.reverse()
      for j in range(k):
        list_new_word[i+j]=list_result_word[j]
      newWord=''.join(list_new_word)
      if newWord not in visited:
        visited.add(newWord)
        q.append((newWord,cnt+1))

result=-1
bfs()
print(result)