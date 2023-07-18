# 1~9까지의 숫자 중 하나를 입력하면 그 단의 구구단 결과를 한 줄에 출력하는 프로그램을 작성하세요.

# >> 입력

# 2


# >> 출력

# 2 4 6 8 10 12 14 16 18

# 내가 푼것
n = int(input("몇단을 출력할까요 : "))
for i in range(1, 10):
    print(n*i, end=' ')

# 답안
n = int(input())
for i in range(1, 10):
	print(n*i, end = ' ')