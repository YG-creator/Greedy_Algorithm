'''
#1)
N = int(input('설탕 kg : '))
num_5 = N //5
num_3 = N //3
a = []
b = []
c= [5000]
for i in range (num_5+1) :
    for j in range (num_3+1) :
        if 5*i + 3*j == N :
            list.append(a,i)
            list.append(b,j)
            for i in range(len(a)) :
                list.append(c, a[i] + b[i])
if c == [5000] :
    print(-1)
else:
    print(min(c))
'''

#2
N = int(input('설탕 kg : '))
count = 0
while N > 0 :
    if N % 5 == 0 :
        N -= 5
        count += 1
    elif N % 3 == 0:
        N -= 3
        count += 1
    elif N>5 :
        N -= 5
        count += 1
    else :
        count = -1
        break
print(count)
