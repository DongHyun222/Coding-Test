#프로그래머스 92342 
#카카오 2019년 공채 level2문제
#조합을 활용해서 전체 경우의수 확인 

from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    combi = []
    for i in range(1,col+1):
        combi.extend(combinations(range(col),i))    #종목별로 만들 수 있는 모든 조합의 개수 찾기
        # print(combi)
    
    unique = []
    for i in combi:
        # tmp = [tuple([item[key] for key in i]) for item in relation]
        # 주어진 키로 리스트의 index별 아이템 뽑아내기
        tmp = []
        for item in relation:
            new_tuple = []
            
            for key in i:
                new_tuple.append(item[key])
            tmp.append(tuple(new_tuple))
        
        if len(set(tmp)) == row:
            put = True
            for x in unique:
                if set(x).issubset(set(i)):
                    put = False
                    break
            if put:
                unique.append(i)
    
    return len(unique)