N = int(input())
A,B,C,D,E,F = map(int,input().split())
if N == 1 :
    print(sum[A,B,C,D,E,F])-max([A,B,C,D,E,F])
else :
    sum3 = min(list(map(sum, [[A,B,C], [A,B,D], [A,E,D], [A,E,C], [F,B,C], [F,B,D], [F,E,C], [F,E,D]])))
    sum2 = min(list(map(sum, [[A,B], [A,C],  [A,D], [A,E], [B,C], [B,D], [E,C], [E,D], [F,B], [F,C], [F,E], [F,D]])))
    sum1 = min([A,B,C,D,E,F])
    print(sum3*4 + sum2*(8*N - 12) + sum1*(5*N**2-16*N+12))
