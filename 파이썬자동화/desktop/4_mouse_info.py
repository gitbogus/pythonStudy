li = ['Korea', 'America', 'China']  # li 초기화

print(li[0])

cnt = 0
str01 = ''

for i in li:
    for j in i:
        str01 += j[0]                              # j[0]을 str01에 추가

        cnt = cnt + 1                                     # a를 1 증가 시킴

        if cnt > 5:                                       # a가 5보다 크면

            break                                       # 안쪽 for 반복문을 멈춤 

   # 화면에 출력
print(i)
print(j)