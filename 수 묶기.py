N = int(input())
a = []              #입력 숫자 리스트
for _ in range(N) :
    a.append(int(input()))
b = sorted(a)       #오름차순 정렬

for i in range(N) : #1보다 큰 수 index 구하기
    if b[i] > 1 :
        index = i
        break
ans = 0
for i in range(0,index) :     # 1보다 작은 수는 더하기
    ans += b[i]
for j in range(index,N,2) :   # 1보다 큰 수는 묶고 더하기
    if j == N - 1 :           # 마지막 index는 더하기
        ans += b[j]
    else :
        ans += b[j]*b[j+1]    
print(ans)
