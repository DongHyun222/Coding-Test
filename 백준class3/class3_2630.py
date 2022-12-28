N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

white,blue = 0,0

def solution(x,y,M):
    global white,blue
    first = graph[x][y]
    for i in range(x,x+M):
        for j in range(y,x+M):
            if graph[i][j] != first:
                solution(x,y,M//2)
                solution(x,y+M//2,M//2)
                solution(x+M//2,y,M//2)
                solution(x+M//2,y+M//2,M//2)
                return
    if first == 1:
        blue += 1
    else:
        white += 1

solution(0,0,N)
print(white)
print(blue)

