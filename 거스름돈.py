money = int(input())            #가격
receive = 1000 - money          #잔돈
a = [500,100,50,10,5,1]         #동전 종류
count = 0
for i in range(6) :
    count += (receive //a[i])   #동전 갯수
    receive %= a[i]
print(count)
