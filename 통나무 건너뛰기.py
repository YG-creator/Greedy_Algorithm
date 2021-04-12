T=int(input())                              #테스트 케이스 갯수
for i in range(T):
    N=int(input())                          #통나무 갯수
    trees=list(map(int,input().split()))    #통나무 높이
    trees.sort()                            #정렬
    result=0                                #답
    for j in range(2, N):                   #인덱스 차가 2인 것끼리의 차
        result=max(result,abs(trees[j]-trees[j-2]))
    print(result)
