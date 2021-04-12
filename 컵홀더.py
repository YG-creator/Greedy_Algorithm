N = int(input())                        #좌석 갯수
cnt = N + 1                             #컵홀더 갯수
seat = input()                          #좌석 상황
seat_indx = 0                                   #
while(1) :    
    if seat[seat_indx] == seat[seat_indx +1] == 'L' :
        cnt -= 1
        seat_indx += 2
    else :
        seat_indx += 1
    if seat_indx == N :
        break
print(cnt)
