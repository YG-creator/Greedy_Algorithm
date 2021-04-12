N,K = list(map(int,input().split()))            #보석 갯수, 가방 갯수
M = []
V = []
for i in range(N) :
    a = list(map(int,input().split()))
    M.append(a[0])                              #보석 무게
    V.append(a[1])                              #보석 가격
C = []                                          #가방 종류
D = []                                          #가져갈 보석 가격
total = 0                                       # 총 가격
for _ in range(K) :
    C.append(int(input()))
for i in C :
    for j in range(N) :
        if i > M[j] :
            D.append(V[j])
    total += max(D)
    V[V.index(max(D))] = 0
    D = []
print(total)
