##기출문제
##구현 9번 문자열 압축 
##2020 카카오 신입공채

def solution(s):
    answer = len(s)
    
    for step in range(1,len(s)//2 + 1):
        compressed = ""         ##결과값 저장소
        prev = s[0:step]        ##중복된 문자열 확인값
        cnt = 1                 ##중복 문자열 횟수
        
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                if cnt >= 2:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[j:j+step]
                cnt = 1
        
        if cnt >= 2:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        
        answer = min(answer,len(compressed))
    
    return answer

