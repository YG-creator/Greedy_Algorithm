n, k = map(int, input().split())        #구멍 수, 코드 종류 갯수
s = list(map(int, input().split()))     #코드 종류
m = [0 for i in range(n)]               #꼳힌 코드
cnt = 0
for i in range(k):                      #꼳을 코드 종류               
    isTrue = False
    for j in range(n):                  #구멍 비어 있고 종류가 다르면 꼳기
        if m[j] == s[i] or m[j] == 0:
            isTrue = True
            m[j] = s[i]
            break
    if isTrue:                          
        continue
    else:                               #같은게 없고 빈곳이 없을경우
        a = 0
        for j in range(n):                      #꼳힌 코드
            try:
                if a < s[i + 1:].index(m[j]) :
                    a = s[i + 1:].index(m[j])
                    b = j
            except:
                a = -1
                b = j
                break
        m[b] = s[i]
        cnt += 1
print(cnt)

