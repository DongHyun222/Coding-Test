#기출문제
#정렬 25번
#카카오 2019 신입공채, 프로그래머스 42889번

def solution(N, stages):
    answer = []
    lst = [0] * (N+1)
    stages.sort()

    cnt = 0
    len_stages = len(stages)

    for i in range(1,len(lst)):     #스테이지 실패율 lst에 저장
        if len_stages == 0:
            break
        x = stages.count(i)
        lst[i] = x/len_stages
        len_stages -= x

    sub_ans = []

    for i in range(1,len(lst)):
        sub_ans.append([i,lst[i]])
    sub_ans.sort(key=lambda x:-x[1])

    for i in range(len(sub_ans)):
        answer.append(sub_ans[i][0])
    
    return answer
print(solution(5,[2,1,2,6,4,3,3]))

'''
def solution(N, stages):
    answer = []
    lst = [0] * (N+1)
    
    stages.sort()
    cnt = 1
    stages_len = len(stages)
    for i in range(len(stages)):
        if (i+1) != len(stages) and stages[i] == stages[i+1]:
            cnt += 1
        elif stages[i] < N:
            lst[stages[i]] = cnt/stages_len
            stages_len -= cnt
            cnt = 1
        elif cnt == len(stages):
            answer.append(N)
            for j in range(1,N):
                answer.append(j)
            return answer
    
    sub_ans = []
    for i in range(1,len(lst)):
        sub_ans.append([i,lst[i]])
    
    sub_ans.sort(key=lambda x: -x[1])
    
    for i in range(len(sub_ans)):
        answer.append(sub_ans[i][0])
    
    return answer
print(solution(5,[4,1,1,2,3,5,6]))'''