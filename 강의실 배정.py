N = int(input())
T = [list(map(int,input().split())) for _ in range(N)]
T.sort()
cnt = 1
fin = T[0][1]
for i in range(1,N) :
    if T[i][0] >= fin :
        fin = T[i][1]
        cnt +=1
print(cnt)
