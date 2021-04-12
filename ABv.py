A,B = map(int,input().split())                  #입력
count = 1
while(1):
    if A == B:                                  #A=B이면 끝
        break
    elif A > B or (B % 10 >= 3 and B % 2 != 0): #마지막 숫자가 3이상 홀수 인경우
        count = -1                              #A>B 인경우 제외
        break
    elif B % 10 == 1:                           #마지막 숫자가 1인경우 10으로 나눔 
        B //= 10
        count+=1
    elif B % 2 == 0:                            #마지막 숫자가 짝수인 경우 2로 나눔
        B //= 2
        count+=1
print(count)
