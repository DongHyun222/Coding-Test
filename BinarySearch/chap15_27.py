#기출문제
#이진탐색 변형?문제
#리스트에서 x로 시작하는점과 끝점을 찾아서 크기반환

N,x = map(int,input().split())
lst = list(map(int,input().split()))

def first(lst,target,start,end):
    if start>end:
        return None
    mid = (start+end) // 2

    if (mid == 0 or target > lst[mid-1]) and lst[mid] == target:        #구한 인덱스-1한 위치의 값이 타겟보다 작아야됨
        return mid
    elif lst[mid] >= target:
        return first(lst,target,start,mid-1)
    else:
        return first(lst,target,mid+1,end)

def last(lst,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2

    if (mid == N-1 or target < lst[mid+1]) and lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return last(lst,target,start,mid-1)
    else:
        return last(lst,target,mid+1,end)

def ans(lst,x):
    n = len(lst)

    lt = first(lst,x,0,n-1)
    
    if lt == None:
        return 0
    
    rt = last(lst,x,0,n-1)

    return rt-lt+1

cnt = ans(lst,x)
if cnt == 0:
    print(-1)
else:
    print(cnt)
