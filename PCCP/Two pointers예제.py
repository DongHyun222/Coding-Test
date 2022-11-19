#PCCP시험대비 Two pointers예제
#defaultdict를 통해 보석 종류가 다 있는지 확인

import collections
def solution(gems):
    answer = [0,0]
    sH = collections.defaultdict(int)
    left = 0
    k = len(set(gems))      #보석종류 k개
    maxL = 100000000        #최소 길이 저장

    for right in range(len(gems)):
        sH[gems[right]] += 1
        if len(sH) == k:    #보석종류가 k개일때
            while True:
                if len(sH) < k:
                    break
                if right-left+1 < maxL:     #최소 구간 저장
                    maxL = right-left+1
                    answer = [left+1,right+1]
                
                sH[gems[left]] -= 1
                if sH[gems[left]] == 0:
                    del sH[gems[left]]
                left += 1
    
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))