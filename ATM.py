#1

n = int(input('사람 수 : '))
time = list(map(int,input().split()))
total_time = 0
time.sort()  #오름차순
'''for i in range(n) :  #오름차순 (선택정렬)
    min = time[i]
    for j in range(i+1,n) :
        if min > time[j] :
            temp = time[j]
            time[j] = min
            min = temp
    time[i] = min
'''
for i in range(n) :
    for j in range(0,i+1) :
        total_time += time[j]
print(total_time)


#알아낸거
'''
map(int,문자열) -> 다 int 형으로 변환
문자열.split()
리스트.sort() -> 오름차순
선택정렬
