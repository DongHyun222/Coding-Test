N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

ans_minus = 0
ans_zero = 0
ans_plus = 0

def dfs(x,y,n):
    global ans_minus, ans_plus, ans_zero

    num_check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        #9등분해서 다시 재귀탐색
                        dfs(x+k*n//3, y+l*n//3,n//3)
                return  #재귀탐색 끝나면 리턴
    
    if num_check == -1:
        ans_minus += 1
    elif num_check == 0:
        ans_zero += 1
    else:
        ans_plus += 1

dfs(0,0,N)
print(ans_minus)
print(ans_zero)
print(ans_plus)