# 입출력

# 입력 : 1 2 3 4 5
# 출력 : 5 4 3 2 1

# 입력 : 2 4 6 7 8
# 출력 : 8 7 6 4 2

# 내가푼것
# number = input()
# re = (number[::-1])
# print(re)

# 답안
n = input()

l = list(n.strip().split())
len1 = len(l) - 1
for i in range(len1, -1, -1):
	print(l[i], end=' ')