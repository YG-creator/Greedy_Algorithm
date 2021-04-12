'''
R,C = map(int,input().split())          #행,열 수
pipe = []                               #파이프 상황
c = []                                  #지나간 길
d = []                                  #지나갈려고 한 길
cnt = 0
for _ in range(R) :
    pipe.append(input())


for i in range(R) :     #행
    if cnt != 0 :
        break
    j = 0               #열
    while(1) :
        if i == 0 :                         #맨 위
            if pipe[i][j+1] == '.':         #오른 쪽
                j += 1 
            elif pipe[i+1][j+1] == '.':     #아래 대각선
                i += 1
                j += 1                
            else :                          #지나 갈수 없음
                break
        elif i == R - 1 :                   #맨 아래
            if pipe[i-1][j+1] == '.':       #위 대각선                
                i -= 1
                j += 1            
            elif pipe[i][j+1] == '.':       #오른 쪽
                j += 1       
            else :                          #지나 갈수 없음
                break
        else :                              #중간
            if pipe[i-1][j+1] == '.':       #위 대각선                
                i -= 1
                j += 1            
            elif pipe[i][j+1] == '.':       #오른 쪽
                j += 1 
            elif pipe[i+1][j+1] == '.':     #아래 대각선
                i += 1
                j += 1                
            else :                          #지나 갈수 없음
                break
            
        d.append([i,j])             #지나간길
        if [i,j] in c :     #지나간 길이면 탈락
            
            d = []
            break   
        if j == C - 1 :         #통과
            cnt += 1        #갯수
            c += d          #지나간 길
            break
c.sort(reverse = True)

for i in range(c[0][0]+1,R) :
    j = 0               #열
    while(1) :
        if i == 0 :                         #맨 위
            if pipe[i][j+1] == '.':         #오른 쪽
                j += 1 
            elif pipe[i+1][j+1] == '.':     #아래 대각선
                i += 1
                j += 1                
            else :                          #지나 갈수 없음
                break
        elif i == R - 1 :                   #맨 아래
            if pipe[i][j+1] == '.':         #오른쪽                
                j += 1            
            elif pipe[i-1][j+1] == '.':     #위 대각선
                i -= 1
                j += 1       
            else :                          #지나 갈수 없음
                break
        else :                              #중간
            if pipe[i][j+1] == '.':         #오른쪽                
                j += 1            
            elif pipe[i-1][j+1] == '.':     #위 대각선
                i -= 1
                j += 1 
            elif pipe[i+1][j+1] == '.':     #아래 대각선
                i += 1
                j += 1                
            else :                          #지나 갈수 없음
                break
            
        d.append([i,j])             #지나간길
        if [i,j] in c :     #지나간 길이면 탈락
            
            d = []
            break   
        if j == C - 1 :         #통과
            cnt += 1        #갯수
            c += d          #지나간 길
            break

   
print(cnt)
'''

def solve(i, j):                                                            
    if j == c-1:                                                            #끝까지 가면 통과
        return True
    
    for d in dx:                                                    
        if 0<=i+d<r and table[i+d][j+1] == '.' and not visit[i+d][j+1]:     #열,행 이내이고 /갈 수 있는 곳이 있고 / 간곳 안가면 통과
            visit[i+d][j+1] = True                                          #지난 곳 true로 
            if solve(i+d, j+1):                                             #끝까지 가면 통과
                return True    

r, c = map(int, input().split())                        #행,열
table = [list(input().rstrip()) for _ in range(r)]      #장애물 상황


visit = [[False] * c for _ in range(r)]                 #지난 곳(true)
dx = [-1, 0, 1]                                         #행 위,중간,아래
ans = 0                                                 #파이프 갯수
for i in range(r):
    if table[i][0] == '.':
        if solve(i, 0):                                 #끝까지 가면
            ans += 1
print(ans)

