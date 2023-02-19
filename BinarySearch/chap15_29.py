#이진탐색 29번 공유기 설치
#가장 인접한 두 공유기 사이의 거리를 최대로

N,C = map(int,input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

start = 1
end = lst[-1] - lst[0]
result = 0

while start <= end:
    mid = (start + end) // 2    #mid 는 가장 인접한 공유기 사이거리
    value = lst[0]
    cnt = 1

    for i in range(1,N):
        if lst[i]- value >= mid:
            value = lst[i]
            cnt += 1

    if cnt >= C: 
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)