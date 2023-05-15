import sys
input = sys.stdin.readline

N,M = map(int,input().split())
# 8x8 체스판 만들기, 맨 왼쪽 위에 칸이 검정 or 흰색

graph = []
for _ in range(N):
    graph.append(list(input()))

def count_ans(a,b):   #W로 시작할때
    cnt1 = 0 
    cnt2 = 0
    for i in range(a,a+8):
        for j in range(b,b+8):
            # print(i,j)
            if (i+j) % 2 == 0 and graph[i][j] == 'W':
                continue
            elif (i+j) % 2 == 1 and graph[i][j] == 'B':
                continue
            else:
                cnt1 += 1
    
    for i in range(a,a+8):
        for j in range(b,b+8):
            if (i+j) % 2 == 0 and graph[i][j] == 'B':
                continue
            elif (i+j) % 2 == 1 and graph[i][j] == 'W':
                continue
            else:
                cnt2 += 1

    return min(cnt1,cnt2)
    
ans = 1e9
for x in range(N-7):
    for y in range(M-7):
        ans = min(ans,count_ans(x,y))
print(ans)

