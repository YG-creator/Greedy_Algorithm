n = int(input())                            #저울 갯수
s = list(map(int, input().split())).sort()  #저율 종류
num = 1                                     #측정 불가 최소값
for i in range(n):
    if num < s[i]:
        break
    num += s[i]
print(num)
    
