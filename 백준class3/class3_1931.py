#백준 class3 1931번 
#정렬문제

N = int(input())

lst = []

for _ in range(N):
    lst.append(list(map(int,input().split())))
lst.sort(key=lambda x: (x[1],x[0]))     #회의 끝나는 시간이 같으면 시작시간을 비교하자!!!

start = lst[0][1]
cnt = 1
for i in range(1,N):
    if lst[i][0] >= start:
        cnt += 1
        start = lst[i][1]
print(cnt)
