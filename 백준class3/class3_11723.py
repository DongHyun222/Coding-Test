

import sys
input = sys.stdin.readline

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
visited = [0] * 21
N = int(input())

for _ in range(N):
    a = input().split()
    if a[0] == "all":
        visited = [1] * 21
        continue
    elif a[0] == "empty":
        visited = [0] * 21
        continue
    a[1] = int(a[1])
    if a[0] == "add":
        visited[a[1]] = 1
    elif a[0] == "check":
        if visited[a[1]] == 1:
            print("1")
        else:
            print("0")
    elif a[0] == "remove":
        if visited[a[1]] == 1:
            visited[a[1]] = 0
    elif a[0] == "toggle":
        if visited[a[1]] == 1:
            visited[a[1]] = 0
        else:
            visited[a[1]] = 1
    

