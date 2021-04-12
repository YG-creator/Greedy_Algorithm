a = []      #case 순서
b = []      #최대 사용일
cnt = 0
while (1) :
    L,P,T = list(map(int,input().split()))
    if (L * P * T) == 0 :
        break
    n = 0
    n += (T // P) * L
    if T % P < L :
        n += (T % P)
    else :
        n +=  L
    a.append(n)
    cnt += 1
    b.append(cnt)

for i in range(len(a)) :    
    print(f'Case {b[i]}: {a[i]}')
