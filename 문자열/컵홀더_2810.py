# 컵홀더_2810_문자열

n=int(input())
member=input()

cnt=member.count("LL")

print(len(member) if cnt<=1 else len(member)-cnt+1)
