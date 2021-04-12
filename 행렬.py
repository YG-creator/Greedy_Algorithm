N,M = list(map(int,input().split()))    #행렬 크기
change_matrix = [''] * N        #바꿀 행렬
result_matrix = [''] * N        #바뀔 행렬

for i in range(N) :
    change_matrix[i] = list(map(int,input()))       ############틀림
for i in range(N) :
    result_matrix[i] = list(map(int,input()))

cnt = 0                                 #바꾸는 횟수
while change_matrix != result_matrix :
    for i in range(0,N-2) :             #시작 행
        for j in range(0,M-2) :         #시장 열
            if change_matrix[i][j] != result_matrix[i][j] :
                row = i
                col = j
    for k in range(row,row+3) :         #3x3 행렬 바꾸기
        for t in range(col,col+3) :
            change_matrix[k][t] = 1 - change_matrix[k][t]   ########틀림
    cnt += 1                            
    if cnt == (N-2)*(M-2)+1 :
        cnt = -1
        break       
print(cnt)


