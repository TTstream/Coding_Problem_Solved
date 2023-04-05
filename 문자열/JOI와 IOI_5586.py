# JOI와 IOI_5586_문자열

s=input()
JOI=IOI=0
for i in range(len(s)-2):
  if s[i:i+3]=="JOI":
    JOI+=1
  if s[i:i+3]=="IOI":  
    IOI+=1
print(JOI)
print(IOI)