#Programmers고득점 Kit Stack 1번문제
#그냥 무난한 문제

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in arr:
        if i == answer[-1]:
            continue
        else:
            answer.append(i)
    
    
    return answer