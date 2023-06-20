# 애너그램_6996_문자열

for _ in range(int(input())):
  a,b=input().split()
  if sorted(a)==sorted(b):
    print(f'{a} & {b} are anagrams.')
  else:
    print(f'{a} & {b} are NOT anagrams.')
