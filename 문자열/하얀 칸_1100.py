# 하얀 칸_1100_문자열

arr=[list(map(str,input())) for _ in range(8)]
print(sum([1 for i in range(8) for j in range(8) if (i+j)%2==0 and arr[i][j]=='F']))