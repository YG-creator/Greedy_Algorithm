N = int(input())                #카드 묶음 종류 갯수
a = []                          #카드 묶음 종류
for _ in range(N) :
    a.append(int(input()))
b = sorted(a)                   #카드 묶음 종류 오름차순 정렬
c = 0
for i in range(0,N,2) :         #앞에 더한걸 카드 묶음 종류에 추가
    if i == N - 1 :
        break
    c += b[i] + b[i+1]
    b.append(c)
ans = 0
for j in range(len(b)) :        #다 더하기
    ans += b[j]
print(ans)
