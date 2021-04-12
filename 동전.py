N,K = map(int,input().split())   # 동전 종류 갯수, 금액 입력
A = [0]*N
for i in range(N) :             # 동전 종류
    A[i] = int(input())
count = 0
for i in range(N) :
    count += (K // A[N-i-1])
    K %= A[N-i-1]
print(count)                    #총 동전 수 출력
