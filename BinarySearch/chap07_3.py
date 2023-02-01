N,M = map(int,input().split())

lst = list(map(int,input().split()))

start = 0
end = max(lst)
ans = 0

while start<=end:
    cnt = 0
    mid = (start+end) // 2
    for i in lst:
        if i > mid:
            cnt += i-mid
    
    if cnt < M:
        end = mid-1
    else:
        ans = mid
        start = mid+1
print(ans)

