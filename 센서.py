N = int(input())                            #센서의 개수
K = int(input())                            #집중국의 개수
location = list(map(int,input().split()))   #센서 위치
location.sort()                             #센서 위치 오른차순
dis = []                                    #센서 거리 
sum = 0                                     #거리 총합
for i in range(N-1) :                       
    dis.append(abs(location[i] - location[i+1]))
dis.sort(reverse = True)                    #센서 거리 내림차순
for i in range(K-1) :                       #센서 최대거리 0 으로 K-1번
    dis[i] = 0
for i in range(len(dis)) :                  #센서거리 더하기
    sum += dis[i]
print(sum)

