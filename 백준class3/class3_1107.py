#백준 클래스3 1107번
#브루탈포스 (경우의 수 다 세보자 제발)

N = int(input())        #이동하려는 채널
M = int(input())        #고장난 버튼 수
broken_lst = list(map(int,input().split()))        #고장난 버튼

min_cnt = abs(100-N)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken_lst:      #고장났으면 break
            break
        
        elif j == len(nums) - 1:
            min_cnt = min(min_cnt, abs(int(nums)-N) + len(nums))      #최소값갱신
print(min_cnt)
