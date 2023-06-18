#programmers 77485번
#Dev-Matching 웹 백엔드 상반기
#좀 더럽게 풀긴 했는데 회전하는 행렬을 lst에 저장하고 한칸씩 밀어서 저장

def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = (j+1) + (i*columns)
    
    result = []
    
    for q in queries:
        x1,y1,x2,y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        lst = []
        
        for y in range(y1,y2+1):
            lst.append(graph[x1][y])
        for x in range(x1+1,x2+1):
            lst.append(graph[x][y2])
        for y in range(y2-1,y1-1,-1):
            lst.append(graph[x2][y])
        for x in range(x2-1,x1,-1):
            lst.append(graph[x][y1])
        
        answer.append(min(lst))
        
        graph[x1][y1] = lst[-1]
        idx = 0
        while True:
            for y in range(y1+1,y2+1):
                graph[x1][y] = lst[idx]
                idx += 1
            for x in range(x1+1,x2+1):
                graph[x][y2] = lst[idx]
                idx += 1
            for y in range(y2-1,y1-1,-1):
                graph[x2][y] = lst[idx]
                idx += 1
            for x in range(x2-1,x1,-1):
                graph[x][y1] = lst[idx]
                idx += 1
            break
    
    
    return answer