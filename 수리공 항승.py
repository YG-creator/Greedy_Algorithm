N,L = list(map(int,input().split()))
M = sorted(list(map(int,input().split())))
cnt = 0
for i in range(0,N,2) :
    if i == N-1 :
        cnt += 1
        break
    a = (M[i+1] - M[i]) // L 
    cnt += a
    b = (M[i+1] - M[i]) % L
    if 0 < b < L :
        cnt += 1
print(cnt)    


