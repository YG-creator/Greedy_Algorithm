a = input()
b = a.split('-')                 #'-'기준으로 자르기
num = []
for i in b :                    
    c = i.split('+')            #'+'기준으로 자르기
    add = 0
    for j in c :
        add += int(j)
    num.append(add)             #덧셈
mini = num[0]
for i in range(1,len(num)) :
    mini -= num[i]
print(mini)
