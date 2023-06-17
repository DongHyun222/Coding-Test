#프로그래머스 92342 
#카카오 2022년 공채 level2문제
#dfs로 전체 탐색해서 라이언이 큰 점수차로 이기면 answer에 저장

def solution(n, info):
    answer = []
    lst = [i for i in range(10,-1,-1)]
    result = [0]*11
    diff = 0
    
    def dfs(level, idx):
        nonlocal diff, answer, result
        
        if n == level:  #n개만큼 화살을 쐈을때
            a_cnt, r_cnt = 0,0
            for i in range(11):
                if info[i] == 0 and result[i] == 0:
                    continue
                elif info[i] >= result[i]:
                    a_cnt += lst[i]
                else:
                    r_cnt += lst[i]
                    
            if r_cnt > a_cnt:
                sub_diff = r_cnt-a_cnt
                if sub_diff > diff:
                    diff = sub_diff
                    answer = result[:]
                elif sub_diff == diff:
                    for i in range(10,-1,-1):
                        if result[i] < answer[i]:
                            break
                        if result[i] > answer[i]:
                            answer = result[:]
                            break
            return
                
        for i in range(idx,11):
            result[i] += 1
            dfs(level+1, i)
            result[i] -= 1
    
    dfs(0,0)
    
    return answer if answer else [-1]