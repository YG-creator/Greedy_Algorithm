T = int(input())                        #거스름돈 갯수
C = [int(input()) for _ in range(T)]    #거스름돈 종류
M = [25,10,5,1]                         #동전 종류
for i in range(T) :
    a= []
    for j in range(4) :
        a.append(C[i] // M[j])
        C[i] %= M[j]
    print(f'{a[0]} {a[1]} {a[2]} {a[3]}')

