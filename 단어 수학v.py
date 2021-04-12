word_num = int(input())     #단어 갯수
word_list = []              #단어 리스트
for _ in range(word_num) :
    word_list.append(input())
word_ten_dct = {}               #단어 : 10^n   딕셔너리

for word in word_list :        #단어
    cnt = 0
    for alpha in i :            #단어 알파벳
        if j not in word_ten_dct :
            word_ten_dct[alpha] = 10 ** (len(word)-cnt-1)       #새로운 문자면 10^자릿수 
         else :
            word_ten_dct[alpha] += 10 ** (len(word)-cnt-1)      #있는 문자면 + 10^자릿수
        cnt += 1
        
digit_list = sorted(list(word_ten_dct.values()),reverse = True)     #내림차순 정렬

sum = 0
for i in range(len(digit_list)) :       #큰 자릿수 * 큰수(9이하)
    sum += digit_list[i] * (9 - i)
print(sum)  
