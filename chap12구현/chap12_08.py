##기출문제
##구현 8번 문자열 재정렬

x = input()
result = []
cnt = 0

for i in x:
    if i.isalpha():
        result.append(i)
    else:
        cnt += int(i)
result.sort()

if cnt != 0:
    result.append(str(cnt))

print(''.join(result))
