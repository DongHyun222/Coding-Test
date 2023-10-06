#Programmers고득점 Kit Hash 1번문제
#해쉬 쓸필요도 없는 간단한 문제인듯

def solution(nums):
    answer = 0
    
    nums.sort()
    idx = -1
    
    for num in nums:
        if num != idx:
            idx = num
            answer += 1
    
    if answer > len(nums)//2:
        answer = len(nums)//2
    
    return answer