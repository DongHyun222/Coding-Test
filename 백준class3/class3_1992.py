n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

def solution(x,y,n):
    check = graph[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:  
                #다르면 4분할
                print("(",end="")
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                print(")",end="")
                return
    
    if check == 0:   #모두 0일때
        print("0",end="")
        return
    else:   #모두 1일때
        print("1",end="")
        return

solution(0,0,n)
