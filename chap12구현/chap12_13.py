#기출문제
#구현 13번 백준 15686번
#삼전 SW역량테스트, 조합사용

from itertools import combinations

N,M = map(int,input().split())

graph = []

for _ in range(N):
    lst = list(map(int,input().split()))
    graph.append(lst)

chicken_dir = []
home_dir = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:        #치킨집
            chicken_dir.append((i,j))
        elif graph[i][j] == 1:      #일반집
            home_dir.append((i,j))

result = []

#조합으로 전체 치킨집중에 M개 뽑음 
candidate = list(combinations(chicken_dir,M))

for candi in candidate:
    cnt = 0
    for ix,iy in home_dir:
        dist = 99999999999999
        for dx,dy in candi:
            #치킨집까지 거리 최소값을 최신화
            dist = min(dist,abs(ix-dx)+abs(iy-dy))
        cnt += dist
    result.append(cnt)
print(min(result))
