#PCCP시험대비 Array예제
#차량 시간에 따른 요금문제

import math
def solution(fees,records):
    #fees -> [기본요금(분) / 기본요금(원) / 단위시간(분) / 단위요금(원)]
    #records -> "HH:MM  차량번호  IN이나OUT"
    inTime = [0] * 10000        #들어온 시간
    isln = [0] * 10000          #차량 들어왔으면 1 아니면 0
    sumTime = [0] * 10000       #시간합 저장
    answer = []

    for record in records:
        a,b,c = record.split(" ")
        h,m = map(int,a.split(":"))

        if c == "IN":           #차량이 들어올 경우 
            inTime[int(b)] = h * 60 + m
            isln[int(b)] = 1
        else:
            sumTime[int(b)] += (h * 60 + m) - inTime[int(b)] 
            isln[int(b)] = 0

    for i in range(10000):
        if isln[i] == 1:
            sumTime[i] += (23*60+59) - inTime[i]
        if sumTime[i] > 0:
            answer.append(fees[1] + max(math.ceil((sumTime[i] - fees[0]) / fees[2]),0)*fees[3])
    
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
