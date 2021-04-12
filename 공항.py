G = int(input())                        #게이트 수
P = int(input())                        #비행기 수
g = [int(input()) for _ in range(P)]    #도킹 상황
cnt = 1                                 #도킹 수
a = g[0]                                #처음 게이트
for i in range(P) :                     #이전 게이트와 다르면 +1
    if a != g[i] :
        cnt +=1
        a = g[i]
print(cnt)
