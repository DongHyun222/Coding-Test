import sys
input = sys.stdin.readline

N,M = map(int,input().split())      #사람,파티수
known = set(input().split()[1:])  #진실아는사람수와 번호

party = []
for _ in range(M):  #파티
    party.append(set(input().split()[1:]))
# print(party)
for _ in range(M):
    for parties in party:
        if len(parties.intersection(known)) != 0:
            known = known.union(parties)
            # print(known)

cnt = 0
for p in party:
    if len(known.intersection(p)) == 0:
        cnt +=1

print(cnt)
