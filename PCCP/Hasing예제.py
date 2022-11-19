#PCCP시험대비 Hashing예제
#defaultdict를 활용하여 카운트한 예제

import collections
def solution(id_list,report,k):
    answer = [0] * len(id_list)
    report = list(set(report))
    reportHash = collections.defaultdict(set)       #유저가 신고한 사람 dict에 저장
    stoped = collections.defaultdict(int)           #신고당한사람 카운트

    for reports in report:
        front,back = reports.split(" ")
        reportHash[front].add(back)
        stoped[back] += 1

    for name in id_list:
        cnt = 0     #몇번 신고당했는지 카운트하여 k보다 크면 answer에저장
        for user in reportHash[name]:
            if stoped[user] >= k:
                cnt += 1
        answer[id_list.index(name)] = cnt

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))

