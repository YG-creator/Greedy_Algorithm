S = input()                 #문장
N = len(S)                  #문장 길이
a = [0,0]                   #연속된 값 갯수
a_indx = 0                     #
for i in range(N-1) :
    if S[i] == S[i+1] :
        a[a_indx] += 1
    else :
        a_indx = 1 - a_indx
print(min(a))
        
