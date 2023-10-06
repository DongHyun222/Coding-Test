#Programmers고득점 Kit Hash 2번문제
#처음에 해쉬안쓰고 이중포문쓰다가 효율성에서 나가리됨
#그냥 하라는데로 해쉬 써서 풀자

def solution(participant, completion):
    dic = {}
    cnt = 0
    
    for part in participant:
        dic[hash(part)] = part
        cnt += hash(part)
        
    for com in completion:
        cnt -= hash(com)
    
    return dic[cnt]