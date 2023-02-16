#이진탐색 28번 고정점 찾기 문제
#재귀문 안에서 다음 재귀로 넘어갈때 return값 꼭쓰자

N = int(input())
lst = list(map(int,input().split()))
cnt = 0

def binary(lst,start,end):
    global cnt
    mid = (start+end) // 2
    cnt += 1

    if lst[mid] == mid:
        return mid
    elif cnt > N//2:
        return -1
    else:
        if lst[mid] > mid:
            return binary(lst,start,mid-1)
        else:
            return binary(lst,mid+1,end)

print(binary(lst,0,N))
