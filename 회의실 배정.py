n = int(input())        #회의의 수
start = [0]*n           #시작 시간 갯수
finish = [0]*n          #끝나는 시간 갯수
for i in range(n) :
    start[i],finish[i] = map(int,input().split())    #시작 시간,끝나는 시간
count = 0
next = finish[0]        #끝나는 시간
for i in range(1,n) :   #다음 시작시간>전 끝나는 시간 -> count 1
    if start[i] > next :
        count += 1
        next = finish[i]
print(count+1)          #회의 최대 개수
    
