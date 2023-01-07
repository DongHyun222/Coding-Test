#백준 class3 5525번 
#아래는 50점 위에는 100점 본풀이

N = int(input())
M = int(input())    #s길이
S = str(input())

cnt, i, ans = 0,0,0
while i < (M-1):
    if S[i:i+3] == "IOI":
        cnt +=1
        i +=2
        if cnt == N:
            cnt -= 1
            ans += 1
    else:
        cnt = 0
        i += 1

print(ans)

'''
N = int(input())
M = int(input())    #s길이
S = str(input())
n = 1 + 2*(N)

cnt = 0
for i in range(M-n+1):
    if S[i] == "O":
        continue
    
    flag = 0
    for j in range(i+1,i+n):
        if (j-i)%2 == 0:
            if S[j] != "I":
                flag = 1
                break
        else:
            if S[j] != "O":
                flag = 1
                break
    if flag == 0:
        cnt += 1
print(cnt)
'''