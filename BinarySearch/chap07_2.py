#이진탐색 예제2번

N = int(input())
N_lst = list(map(int,input().split()))
N_lst.sort()

M = int(input())
M_lst = list(map(int,input().split()))

def Binary(lst,ans,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if lst[mid] == ans:
        return mid
    elif lst[mid] > ans:
        return Binary(lst,ans,start,mid-1)
    else:
        return Binary(lst,ans,mid+1,end)
    
for i in M_lst:
    result = Binary(N_lst,i,0,N-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')

