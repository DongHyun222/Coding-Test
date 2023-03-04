#백준 class3 16928번 
#뱀,사다리 문제
#BFS를 이용해서 100번까지 가는 최소값 구하기

from collections import deque
import sys
input = sys.stdin.readline

#사다리가 있는 칸 -> 올라감
#뱀이 있는 칸 -> 내려감

N,M = map(int,input().split())
lst = [i for i in range(101)]     #여기에 사다리,뱀 다 저장
q = deque([1])
visited = [0]*101       #얘가 주사위 횟수 카운트

for _ in range(N):
    a,b = map(int,input().split())
    lst[a] = b
for _ in range(M):
    a,b = map(int,input().split())
    lst[a] = b

while True:
    idx = q.popleft()
    for j in range(1,7):
        next_idx = lst[idx+j]
        if next_idx<=100 and visited[next_idx] == 0:
            if next_idx == 100:
                print(visited[idx]+1)
                #print(visited)
                exit()
            else:
                visited[next_idx] = visited[idx]+1
                q.append(next_idx)

