# 럭키 스트레이트_18406_문자열

s=list(map(int,input()))
len_s=len(s)//2
print("LUCKY" if sum(s[0:len_s])==sum(s[len_s:]) else "READY")
