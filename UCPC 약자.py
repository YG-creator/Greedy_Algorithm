UCPC = list(input().split())            
ans = ''
for i in range(len(UCPC)) :
    if UCPC[i][0].isupper() == True :       
        ans += UCPC[i][0]
if ans == 'UCPC' :
    print('I love UCPC')
else :
    print('I hate UCPC')
