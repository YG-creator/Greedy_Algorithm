N = int(input())            #레벨 갯수
score = []                  #레벨
dec = 0                     #감소 횟수
for _ in range(N) :
    score.append(int(input()))
for i in range(N-1) :
    if score[i] > score[i+1] :
        dec += score[i] - score[i+1] + 1
print(dec)
