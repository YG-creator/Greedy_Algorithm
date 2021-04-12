N,K = map(int,input().split())      #자릿수, 뺄 자릿수 갯수
num = int(input())                    #숫자
hex_num = []                              #각 자리 숫자
hex_num_indx = 0
ans = 0
for i in range(N) :
    hex_num.append(num // (10**(N-1-i)))
    num %= (10**(N-1-i))
for _ in range(K) :                 #K번 최소값 빼기
    hex_num[hex_num.index(min(hex_num))] = 10         
while(1) :                          #뺀 나머지 숫자 더하기
    if hex_num[hex_num_indx] != 10 :
        ans += hex_num[hex_num_indx] * (10 ** (N-K-1))
        K += 1
    hex_num_indx += 1
    if hex_num_indx == N :
        break
print(ans)

