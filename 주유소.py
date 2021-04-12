N = int(input())                        #도시 갯수
a = list(map(int,input().split()))      #거리 길이 리스트
b = list(map(int,input().split()))      #기름 값 리스트
money = a[0]*b[0]                       #총 금액
c = b[0]                                #기름 값 최소값
for i in range(1,N-1) :
    if c > b[i] :
        c = b[i]
    money += c * a[i]
print(money)

