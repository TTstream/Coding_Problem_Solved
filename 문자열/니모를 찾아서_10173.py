# 니모를 찾아서_10173_문자열

while True:
  s=input()
  if s=="EOI":
    break
  print("Found" if "nemo" in s.lower() else "Missing")