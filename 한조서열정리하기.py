N = int(input())
H = list(map(int,input().split()))
a = []
for i in range(N-1) :
    cnt = 0
    for j in range(i,N) :
        if H[i] > H[j] :
            cnt += 1
    a.append(cnt)
print(max(a))
