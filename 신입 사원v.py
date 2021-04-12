import sys

t = int(input())            # 면접수
a = []                      # 출력 리스트

for _ in range(t):
    n = int(input()) # 1 <= n <= 100,000
    lst = sorted([list(map(int, sys.stdin.readline().strip().split())) for x in range(n)],  #성적 순위 기준  오름차순 정렬
		 key = lambda x: x[0])
    cnt = 1                     
    min = lst[0][1]         #면접 순위 초기 최소값

    for i in range(1, n):   # 최소값 보다 작으면 합격
        if lst[i][1] < min:
            min = lst[i][1]
            cnt += 1
    a.append(cnt)           # 최대 합격자 수를 리스에 추가

for i in a :        #출력
    print(i)
