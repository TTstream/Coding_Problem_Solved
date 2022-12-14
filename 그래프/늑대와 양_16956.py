# 늑대와 양_16956_BFS

def bfs(x,y):
    for dx, dy in d:
        X,Y = x+dx,y+dy
        if 0 <= X < R and 0 <= Y < C:
            if graph[X][Y] == 'S':
                return False
            if graph[X][Y] == '.':
                graph[X][Y] = 'D'
    return True

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(R):
    for j in range(C):
        t = True
        if graph[i][j] == 'W':
            t = bfs(i, j)
            if t == False:
                print(0)
                break
if t:
  print(1)
  for line in graph: 
    print(''.join(line))