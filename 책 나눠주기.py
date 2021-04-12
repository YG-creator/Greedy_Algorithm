T = int(input())                                #테스트 케이스 갯수

for _ in range(T):                              
    N, M = map(int,input().split())             #책수, 학생 수
    books = []
    for _ in range(M):
        a, b = map(int, input().split())        #a이상 b 이하 책번호
        books.append( [a, b] )

    # b를 기준으로 정렬 후, 같으면 a로 정렬
    books.sort(key = lambda x: (x[1], x[0]))

    # 정렬한 순서대로 a번의 책을 준다.
    nl = [False for i in range(N+1)]            #false  N번 리스트
    result = 0
    for book in books:                          
        for i in range(book[0], book[1]+1):     #줄 수 있는 책번호 세기
            if nl[i] == False:
                nl[i] = True
                result += 1
                break

    print(result)
